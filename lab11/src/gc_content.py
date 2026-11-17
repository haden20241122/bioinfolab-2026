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

def gc_ratio(seq):
    gc = seq.count('G') + seq.count('C')
    return gc / len(seq)

def mean_quality(qual):
    scores = [ord(ch) - 33 for ch in qual]
    return sum(scores) / len(scores)

reads = read_fastq(sys.argv[1])

# 전체 평균 품질
total_qual = sum(mean_quality(qual) for name, seq, qual in reads)
overall_mean = total_qual / len(reads)

# 각 read의 GC 비율과 평균 품질 계산
results = []
for name, seq, qual in reads:
    gc = gc_ratio(seq)
    mq = mean_quality(qual)
    results.append((name, gc, mq))

# GC 비율 기준 정렬
results.sort(key=lambda x: x[1])

# GC 비율 낮은 10개
low_gc = results[:10]
# GC 비율 높은 10개
high_gc = results[-10:]

print(f"전체 평균 품질: {overall_mean:.4f}")
print()
print("=== GC 비율 낮은 read 10개 ===")
print("read 이름\t\t\tGC 비율\t평균 품질")
for name, gc, mq in low_gc:
    print(f"{name[:30]}\t{gc:.4f}\t{mq:.4f}")

print()
print(f"낮은 GC read들의 평균 품질: {sum(mq for _, _, mq in low_gc) / len(low_gc):.4f}")

print()
print("=== GC 비율 높은 read 10개 ===")
print("read 이름\t\t\tGC 비율\t평균 품질")
for name, gc, mq in high_gc:
    print(f"{name[:30]}\t{gc:.4f}\t{mq:.4f}")

print()
print(f"높은 GC read들의 평균 품질: {sum(mq for _, _, mq in high_gc) / len(high_gc):.4f}")
