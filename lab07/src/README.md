cat > README.md << 'EOF'
# fasta.py 함수 모음

## 함수 목록

### read_fasta(filename)
- **입력**: FASTA 파일 이름
- **출력**: {이름: 서열} 딕셔너리
- **예**: `seqs = read_fasta("data/seqs.fasta")`

### write_fasta(seqs, filename)
- **입력**: {이름: 서열} 딕셔너리, 저장할 파일 이름
- **출력**: 없음 (파일 생성)
- **예**: `write_fasta(seqs, "data/out.fasta")`

### gc_content(seq)
- **입력**: DNA 서열 문자열
- **출력**: GC 비율 (0~1 사이 실수)
- **예**: `gc_content("ATGC")` → `0.5`

### length_stats(seqs)
- **입력**: {이름: 서열} 딕셔너리
- **출력**: 개수, 전체 길이, 평균, 최소, 최대를 담은 딕셔너리
- **예**: `stats = length_stats(seqs)`

### reverse_complement(seq)
- **입력**: DNA 서열 문자열
- **출력**: 역상보 서열 문자열
- **예**: `reverse_complement("ATGC")` → `"GCAT"`

## 부족한 점 / 추가하고 싶은 함수
- GC 함량 필터링 함수
- 서열 길이 히스토그램 출력 함수
- FASTQ 형식 지원
EOF