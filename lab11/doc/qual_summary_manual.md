# qual_summary.py 사용법 및 설명서

## 개요
`qual_summary.py`는 FASTQ 파일을 읽어 전체 read의 평균 품질 점수(Phred score)를 계산하여 출력하는 Python 스크립트이다.

## 사용법
```bash
python src/qual_summary.py <FASTQ 파일 경로>
```

### 실행 예시

```bash
python src/qual_summary.py data/SRR1553607_1.fastq
```