#!/usr/bin/env python3
# shortlines.py - FASTA 파일에서 최소 길이보다 짧은 서열의 개수를 출력한다
# 사용법: python3 src/shortlines.py <FASTA파일> <최소길이>

import sys

if len(sys.argv) < 3:
    print("사용법:", sys.argv[0], "<FASTA파일> <최소길이>")
    sys.exit(1)

if not sys.argv[2].isdigit():
    print("오류: 최소길이는 숫자여야 합니다.")
    sys.exit(1)

filename = sys.argv[1]
minlen = int(sys.argv[2])

count = 0
seq = ""
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith(">"):
            if seq and len(seq) < minlen:
                count += 1
            seq = ""
        else:
            seq += line
    if seq and len(seq) < minlen:
        count += 1

print(count)