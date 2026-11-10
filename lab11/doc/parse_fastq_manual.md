# parse_fastq.py 사용법 및 설명서
`parse_fastq.py`는 FASTQ 형식의 시퀀싱 데이터 파일을 읽고, read의 개수, 첫 번째 read의 이름, 서열, 길이를 출력하는 Python 스크립트이다.

## 사용법
```bash
python src/parse_fastq.py <FASTQ 파일 경로>
```

### 실행 예시
```bash
python src/parse_fastq.py data/SRR1553607_1.fastq
```