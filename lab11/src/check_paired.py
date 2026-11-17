import sys

def read_fastq(filename):
    records = []
    with open(filename) as f:
        lines = f.readlines()
    for i in range(0, len(lines), 4):
        name = lines[i].rstrip()[1:]
        seq = lines[i + 1].rstrip()
        qual = lines[i + 3].rstrip()
        records.append((name, seq, qual))
    return records

def get_base_name(name):
    # 마지막 숫자나 기호 제외하고 같은 이름인지 확인
    # 예: "SRR1553607.1 1 length=101" -> "SRR1553607.1"
    return name.split()[0]

reads1 = read_fastq(sys.argv[1])
reads2 = read_fastq(sys.argv[2])

print(f"파일 1 read 개수: {len(reads1)}")
print(f"파일 2 read 개수: {len(reads2)}")

if len(reads1) == len(reads2):
    print("두 파일의 read 개수가 같습니다.")
else:
    print("두 파일의 read 개수가 다릅니다!")

# 같은 순서의 read끼리 이름이 짝을 이루는지 확인
print("\n=== 처음 5쌍 이름 비교 ===")
mismatch = 0
for i in range(min(len(reads1), len(reads2))):
    name1 = get_base_name(reads1[i][0])
    name2 = get_base_name(reads2[i][0])
    if i < 5:
        print(f"read1: {reads1[i][0]}")
        print(f"read2: {reads2[i][0]}")
        print(f"짝 여부: {name1 == name2}")
        print()
    if name1 != name2:
        mismatch += 1

print(f"총 불일치 쌍: {mismatch}개")
if mismatch == 0:
    print("모든 read가 올바르게 짝을 이루고 있습니다.")
