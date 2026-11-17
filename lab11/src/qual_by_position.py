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

reads = read_fastq(sys.argv[1])

position_scores = {}
position_counts = {}

for name, seq, qual in reads:
    for i, ch in enumerate(qual):
        score = ord(ch) - 33
        if i not in position_scores:
            position_scores[i] = 0
            position_counts[i] = 0
        position_scores[i] += score
        position_counts[i] += 1

print("위치\t평균 품질")
for pos in sorted(position_scores.keys()):
    avg = position_scores[pos] / position_counts[pos]
    print(f"{pos + 1}\t{avg:.2f}")
