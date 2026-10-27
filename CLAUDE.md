# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# 이 저장소의 규칙

## 이 저장소는
생물정보학실험 수업의 실습 저장소이다. 주차별로 labNN 폴더가 있다.
빌드, 린트, 테스트 도구는 없다. 스크립트는 `python3` 또는 `bash` 로 바로 실행한다.

## 폴더 구조
- 새 주차 폴더는 `lab-template` 을 복사해서 만든다 (`cp -r lab-template labNN`). 안에는 `data/`(입력·생성 데이터), `doc/`(보고서, 결과 요약), `src/`(스크립트)가 있다.
- 스크립트는 주차 폴더 안에서 `python3 src/<스크립트>.py <인자>` 처럼 실행한다. 출력 경로도 주차 폴더 기준이다 (예: `check_codespace.sh` 는 `doc/check_result.txt` 에 쓴다).
- 주차 폴더마다 `doc/` 에 README 나 요약 문서(`lab09/doc/README.md`, `lab09/doc/lab07.md`)가 있으며, 파일별 사용법 표가 정리되어 있다.
- `resources/` 에는 수업에서 함께 쓰는 예제 데이터(`data/`)와 셸 스크립트(`src/`)가 있다.

## 공용 FASTA 모듈 (`lab07/src/fasta.py`)
- `read_fasta(filename)` → `{이름: 서열}`. 헤더의 첫 단어를 이름으로 쓰고, 서열은 대문자로 바꾼다.
- 그 밖에 `write_fasta`, `gc_content`, `reverse_complement`, `length_stats` 가 있다.
- lab07 의 스크립트는 `from fasta import ...` 로 가져다 쓴다. 스크립트와 같은 폴더에 있어서 동작하므로, 다른 주차 폴더에서 쓰려면 `sys.path` 에 `lab07/src` 를 추가하거나 `PYTHONPATH` 를 설정해야 한다.
- 이 파일 안에는 `if __name__ == "__main__":` 블록이 두 개 있고, 그 사이와 뒤에 함수가 정의되어 있다. 함수를 추가하거나 고칠 때 이 순서에 유의한다.

## 실행 환경
- Codespaces 의 dev container 를 쓴다 (`.devcontainer/` 아래 1-basic, 2-conda, 3-seq, 4-genome). 주차에 따라 seqkit, blast, mafft, iqtree, fastqc, fastp, shovill, prokka 등이 있을 수도 없을 수도 있다. 어떤 도구가 있는지는 `bash .devcontainer/check.sh` 로 확인한다.
- `$MYHOME` 은 저장소 루트를 가리킨다.
- 시퀀싱 데이터(`*.fastq`, `*.fq.gz`, `*.sra`)와 조립·주석 결과 폴더(`shovill_out/`, `prokka_out/` 등)는 `.gitignore` 로 제외된다. 필요하면 `wget` 으로 다시 받는다.

## 코드를 쓸 때
- FASTA 파일은 lab07/src/fasta.py 의 read_fasta 로 읽는다.
- 새 라이브러리(Biopython 등)를 쓰기 전에 먼저 물어본다.
- 주석은 한국어로 쓴다.
- 기존 코드처럼 표준 라이브러리만 쓰고, 명령행 인자는 `sys.argv` 로 받는다. 표 형식 결과는 TSV(헤더 한 줄 + 탭 구분)로 저장한다.

## 하지 말 것
- rm 으로 파일을 지우지 않는다.
- pip install 로 무언가를 설치하지 않는다. 없는 도구는 강의자에게 알린다 (conda 실습 주차만 예외).
- git 명령어를 실행하지 않는다.
## FASTA 파일을 읽을 때
- lab07/src/fasta.py 의 read_fasta 함수를 쓴다.
- Biopython의 SeqIO는 쓰지 않는다.

## 새 라이브러리를 쓰기 전에
- 먼저 사람에게 물어본다.
- 표준 라이브러리로 해결 가능한지 먼저 확인한다.

## 하지 말아야 할 명령어
- rm 으로 파일을 지우지 않는다.
- pip install 로 무언가를 설치하지 않는다.
- git 명령어를 실행하지 않는다.

## 추가 규칙
- 코드 실행 전에 무엇을 할 것인지 한 줄로 설명한다.