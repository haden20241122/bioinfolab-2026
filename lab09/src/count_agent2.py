"""FASTA 파일의 서열 개수를 출력한다 (lab07/src/fasta.py 의 read_fasta 사용)."""
import os
import sys

# lab07/src 의 공용 FASTA 모듈을 가져오기 위해 경로를 추가한다
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "lab07", "src"))
from fasta import read_fasta


def count_fasta(filename):
    """read_fasta 로 읽은 서열의 수를 센다."""
    return len(read_fasta(filename))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("사용법: python3 src/count_agent2.py <FASTA 파일>")
        sys.exit(1)
    print(count_fasta(sys.argv[1]))
