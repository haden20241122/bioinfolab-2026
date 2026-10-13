import sys
import os
from fasta import read_fasta, gc_content

folder = sys.argv[1]
outfile = sys.argv[2]

with open(outfile, "w") as out:
    out.write("filename\tcount\ttotal\tmean_gc\n")
    for filename in os.listdir(folder):
        if filename.endswith(".fasta"):
            filepath = os.path.join(folder, filename)
            seqs = read_fasta(filepath)
            count = len(seqs)
            total = sum(len(s) for s in seqs.values())
            mean_gc = round(sum(gc_content(s) for s in seqs.values()) / count, 4)
            out.write(filename + "\t" + str(count) + "\t" + str(total) + "\t" + str(mean_gc) + "\n")

print("저장 완료:", outfile)
