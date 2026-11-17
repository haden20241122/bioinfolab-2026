# qual_by_position.py 사용법 및 설명서

## 개요

`qual_by_position.py`는 FASTQ 파일의 모든 read에서 위치별 평균 품질 점수를 계산하여 탭으로 구분된 표 형식으로 출력하는 Python 스크립트이다. 이는 FastQC의 Per base sequence quality 그래프가 계산하는 것과 동일한 값이다.

## 사용법

```bash
python src/qual_by_position.py <FASTQ 파일 경로>
```

### 실행 예시

```bash
python src/qual_by_position.py data/SRR1553607_1.fastq
```

### 출력 예시
