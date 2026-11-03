#!/bin/bash
# NCBI E-utilities(esearch/efetch)로 식물 8종의 rbcL 서열을 받는다.
# db=nuccore 에서 rbcL[Gene] AND 1300:1500[SLEN] 조건으로 검색해
# 첫 번째 검색 결과만 FASTA(.fa), GenBank(.gb) 로 받는다.
set -e

OUTDIR="$(dirname "$0")/../data"
BASE="https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

# "학명(URL 인코딩):파일이름" 쌍
species=(
  "%22Arabidopsis%20thaliana%22:rbcL_arabidopsis"
  "%22Panax%20ginseng%22:rbcL_ginseng"
  "%22Oryza%20sativa%22:rbcL_rice"
  "%22Zea%20mays%22:rbcL_maize"
  "%22Ginkgo%20biloba%22:rbcL_ginkgo"
  "%22Pinus%20thunbergii%22:rbcL_pine"
  "%22Adiantum%20capillus-veneris%22:rbcL_fern"
  "%22Marchantia%20polymorpha%22:rbcL_liverwort"
)

for entry in "${species[@]}"; do
  org="${entry%%:*}"
  name="${entry##*:}"

  term="rbcL%5BGene%5D%20AND%20${org}%5BOrganism%5D%20AND%201300%3A1500%5BSLEN%5D"

  echo "[${name}] esearch..."
  wget -q -O "$OUTDIR/${name}_esearch.xml" \
    "$BASE/esearch.fcgi?db=nuccore&term=${term}&retmax=1"
  sleep 1

  id=$(grep -o '<Id>[0-9]*</Id>' "$OUTDIR/${name}_esearch.xml" | head -1 | sed 's/<[^>]*>//g')

  if [ -z "$id" ]; then
    echo "  경고: ${org} 검색 결과 없음, 건너뜀" >&2
    continue
  fi
  echo "  -> id=${id}"

  echo "[${name}] efetch fasta..."
  wget -q -O "$OUTDIR/${name}.fa" \
    "$BASE/efetch.fcgi?db=nuccore&id=${id}&rettype=fasta&retmode=text"
  sleep 1

  echo "[${name}] efetch genbank..."
  wget -q -O "$OUTDIR/${name}.gb" \
    "$BASE/efetch.fcgi?db=nuccore&id=${id}&rettype=gb&retmode=text"
  sleep 1
done
