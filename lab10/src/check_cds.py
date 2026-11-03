"""lab10/data 의 rbcL_*.gb 파일을 읽어 CDS 번역을 검증한다.

각 파일마다 VERSION, ORGANISM, CDS 위치를 꺼내고, CDS 서열을
codon_start 를 반영해 table=11 로 번역한 결과가 /translation
과 같은지 확인해 TSV 로 출력한다.
"""
import glob
import os

from Bio import SeqIO

DATADIR = os.path.join(os.path.dirname(__file__), "..", "data")


def translate_cds(record, feature):
    """CDS feature 를 codon_start 를 반영해 table=11 로 번역한다."""
    seq = feature.extract(record.seq)
    codon_start = int(feature.qualifiers.get("codon_start", ["1"])[0]) - 1
    seq = seq[codon_start:]
    seq = seq[: len(seq) - len(seq) % 3]
    return str(seq.translate(table=11, to_stop=False)).rstrip("*")


def main():
    files = sorted(glob.glob(os.path.join(DATADIR, "rbcL_*.gb")))

    print("파일", "VERSION", "ORGANISM", "CDS위치", "번역일치", sep="\t")

    for filename in files:
        record = SeqIO.read(filename, "genbank")
        organism = record.annotations.get("organism", "")

        cds_list = [f for f in record.features if f.type == "CDS"]
        if not cds_list:
            print(os.path.basename(filename), record.id, organism, "없음", "NA", sep="\t")
            continue

        for feature in cds_list:
            location = f"{feature.location.start + 1}..{feature.location.end}"
            mine = translate_cds(record, feature)
            given = feature.qualifiers.get("translation", [""])[0]
            match = mine == given
            print(os.path.basename(filename), record.id, organism, location, match, sep="\t")


if __name__ == "__main__":
    main()
