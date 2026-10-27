# lab07 요약: Python 함수와 모듈로 FASTA 다루기

## 핵심 개념
- **함수 정의**: `def 함수이름(인자):` → `"""설명"""` → `return 결과`
- **print와 return의 차이**: `print`는 화면에 출력만 하고 `None`을 돌려준다. `return`은 값을 돌려주므로 변수에 저장하거나 계산에 쓸 수 있다 (`fseqlen.py`).
- **모듈 import**: 공통 함수를 `fasta.py`에 모아 두고 `from fasta import read_fasta, gc_content`로 가져다 쓴다.
- **`if __name__ == "__main__":`**: 파일을 직접 실행할 때만 동작하고, import할 때는 실행되지 않는 코드를 넣는다.
- **파일 쓰기 모드**: `"w"`는 새로 쓰기(기존 내용 삭제, bash의 `>`), `"a"`는 이어 쓰기(bash의 `>>`)
- **명령행 인자**: `sys.argv[1]`, `sys.argv[2]`, ... 숫자로 쓰려면 `int()`로 변환해야 한다.

## 모듈 `src/fasta.py`
| 함수 | 입력 | 출력 |
|------|------|------|
| `read_fasta(filename)` | FASTA 파일 이름 | `{이름: 서열}` 딕셔너리 (헤더의 첫 단어를 이름으로, 서열은 대문자로 변환) |
| `write_fasta(seqs, filename)` | 서열 딕셔너리, 파일 이름 | 없음 (FASTA 파일 생성) |
| `gc_content(seq)` | DNA 서열 | GC 비율 (0~1), 빈 서열이면 0.0 |
| `reverse_complement(seq)` | DNA 서열 | 역상보 서열 (예: `ATGC` → `GCAT`) |
| `length_stats(seqs)` | 서열 딕셔너리 | `count`, `total`, `mean`, `min`, `max` 딕셔너리 |

## 스크립트 (`src/`)
| 스크립트 | 사용법 | 하는 일 |
|----------|--------|---------|
| `fgc.py` | `python3 src/fgc.py` | GC 함량 함수 연습 |
| `fseqlen.py` | `python3 src/fseqlen.py` | print와 return의 차이 확인 |
| `countseq2.py` | `python3 src/countseq2.py <fasta>` | 서열 개수 출력 |
| `seqlen2.py` | `python3 src/seqlen2.py <fasta>` | 서열별 이름과 길이 출력 |
| `stats.py` | `python3 src/stats.py <fasta>` | 개수, 전체/평균/최소/최대 길이 출력 |
| `filter_fasta.py` | `python3 src/filter_fasta.py <in> <최소길이> <out>` | 최소 길이 이상인 서열만 새 FASTA로 저장 |
| `summary.py` | `python3 src/summary.py <fasta> <out.tsv>` | 서열별 `name`, `length`, `gc`를 TSV로 저장 |
| `batchinfo.py` | `python3 src/batchinfo.py <폴더> <out.tsv>` | 폴더 안 `.fasta` 파일마다 `count`, `total`, `mean_gc`를 TSV로 저장 |
| `filter.py` | (작성 중) | `read_fasta`만 정의된 미완성 파일 |

## 데이터와 결과
- `data/seqs.fasta`, `data/seqs2.fasta`: 엽록체 유전자 3개 (gene1 rbcL, gene2 matK, gene3 psbA), 여러 줄 서열 포함
- `data/lower.fasta`: 소문자가 섞인 서열 (대문자 변환 확인용)
- `doc/long.fasta`: 길이 20 이상 필터 결과 (gene1, gene3)
- `doc/summary.tsv`: gene1 30bp/GC 0.5, gene2 15bp/GC 0.4667, gene3 22bp/GC 0.5455
- `doc/batchinfo.tsv`: seqs.fasta·seqs2.fasta 3개/67bp/평균 GC 0.504, lower.fasta 2개/20bp/평균 GC 0.65

## 겪은 오류
- **ZeroDivisionError**: 빈 서열로 GC를 계산할 때 0으로 나눔 → `gc_content`에 길이 0 검사 추가
- **TypeError**: `sys.argv` 값(문자열)을 `int()` 없이 숫자와 비교함

## 남은 과제
- GC 함량으로 필터링하는 함수
- 서열 길이 히스토그램 출력 함수
- FASTQ 형식 지원
- `fasta.py`에 `if __name__ == "__main__":` 블록이 두 번 있어 하나로 합칠 필요가 있음
- `src/README.md`에 `cat > README.md << 'EOF'`와 `EOF` 줄이 그대로 들어가 있음
- `src/write_fasta`는 확장자 없는 중복 파일 (`fasta.py`에 같은 함수가 있음)
