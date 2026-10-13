import sys
from fasta import read_fasta

filename = sys.argv[1]

seqs = read_fasta(filename)

for name in seqs:
    print(name, len(seqs[name]))