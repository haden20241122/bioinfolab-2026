# lab09

## 폴더 구성
```
lab09/
├── data/   입력 데이터 (현재 비어 있음)
├── doc/    문서와 결과 파일
├── junk/   삭제 연습용 빈 파일
└── src/    스크립트
```

## 파일 설명
| 파일 | 사용법 | 설명 |
|------|--------|------|
| `src/count_agent.py` | `python3 src/count_agent.py <fasta>` | FASTA 파일에서 `>`로 시작하는 줄을 세어 서열 개수를 출력 |
| `src/bug1.sh` | `bash src/bug1.sh <폴더>` | 지정한 폴더의 내용을 `ls`로 출력 |
| `src/check_codespace.sh` | `bash src/check_codespace.sh` | Codespace 사용 환경을 확인하고 결과를 `doc/check_result.txt`에 저장 (lab09 폴더에서 실행) |
| `doc/lab07.md` | - | lab07 요약 (Python 함수와 모듈로 FASTA 다루기) |
| `junk/a.txt`, `junk/b.txt`, `junk/keep.txt` | - | 빈 파일 |
