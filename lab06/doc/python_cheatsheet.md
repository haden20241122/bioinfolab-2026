# 나의 bash/python 치트시트

## 스크립트를 만드는 다섯 단계
1. 터미널에서 직접 실행해 결과 확인 → `grep -c ">" data/seqs.fasta` / python: `sum(1 for l in open("data/seqs.fasta") if l.startswith(">"))`
2. 그 명령어를 스크립트에 그대로 옮기기 (맨 위에 `#!/usr/bin/bash`) / python: 맨 위에 `#!/usr/bin/env python3`
3. 바뀔 값을 변수로 빼기 → `FILE="data/seqs.fasta"` / python: `filename = "data/seqs.fasta"`
4. 변수를 인자로 받기 → `FILE="$1"` / python: `filename = sys.argv[1]`
5. 검사 붙이기 → 인자 없음(`-z`), 파일 없음(`-f`)이면 `exit 1` / python: `if len(sys.argv) < 2:` / `if not os.path.isfile(filename):` → `sys.exit(1)`

## 자주 쓸 것
| 항목 | bash | python |
|------|------|--------|
| 실행 권한 주기 | `chmod 700 src/countseq.sh` | 해당 없음 (python은 권한 불필요) |
| 직전 명령어 성공 여부 | `echo $?` (0 성공, 0이 아니면 실패) | 해당 없음 (터미널 기능) |
| 서열 개수 | `grep -c ">" 파일` | `sum(1 for l in open(f) if l.startswith(">"))` |
| 헤더 빼고 서열만 | `grep -v ">" 파일` | `if not line.startswith(">"):` |
| 결과를 파일로 저장 | `./src/batchinfo.sh data > result.tsv` | 해당 없음 (터미널 리디렉션 기능) |
| 명령어 결과를 변수에 | `N=$(grep -c ">" "$1")` | `n = sum(1 for l in open(filename) if l.startswith(">"))` |
| 실행 과정 추적 | `set -x` 또는 `bash -x 스크립트` | 해당 없음 (디버거 별도) |
| 인자 없으면 종료 | `if [ -z "$1" ]; then echo "사용법: $0 <파일>"; exit 1; fi` | `if len(sys.argv) < 2: print("사용법:", sys.argv[0], "<파일>"); sys.exit(1)` |
| 폴더 / 파일 있는지 | `[ -d "$DIR" ]` / `[ -f "$F" ]` | `os.path.isdir(d)` / `os.path.isfile(f)` |

## 헷갈렸던 것
- **변수 저장은 공백 없이**: bash: `DIR=$1` (O) / `DIR = $1` (X) / python: `dir = sys.argv[1]` (공백 있어도 됨)
- **따옴표**: bash: `"$B"`는 값으로 바뀜, `'$B'`는 글자 그대로 / python: 따옴표 종류 상관없이 문자열
- **출력 없음 ≠ 성공**: bash만 해당 (python은 예외로 오류 표시)
- **파이프의 종료 상태는 마지막 명령어 것**: bash만 해당
- **정수 나눗셈**: bash: `$(( 7 / 15 ))`는 0 → `bc` 필요 / python: `7 / 15`는 0.4666 (자동으로 소수)
- **와일드카드**: bash: `*.fasta`가 글자 그대로 넘어올 수 있음 / python: `glob.glob("*.fasta")`는 빈 리스트 반환

## 내가 실수했던 것
1. **수업 자료의 `$`까지 입력함** → bash만 해당. python은 `>>>` 프롬프트
2. **chmod를 빼먹음** → bash만 해당. python은 `python3 스크립트.py`로 실행
3. **다른 폴더에서 실행함** → bash/python 공통. 현재 위치 항상 확인
4. **`$F` 검사를 for문 바깥에 넣음** → bash만 해당. python은 for문 밖에서도 변수 접근 가능
5. **여러 줄을 한 번에 붙여넣음** → bash/python 공통. 한 줄씩 실행