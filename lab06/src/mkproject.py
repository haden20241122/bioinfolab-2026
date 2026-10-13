#!/usr/bin/env python3
# mkproject.py - 새 프로젝트 폴더 구조를 만드는 스크립트
# 사용법: python3 src/mkproject.py <프로젝트이름>

import sys
import os

if len(sys.argv) < 2:
    print("사용법:", sys.argv[0], "<프로젝트이름>")
    sys.exit(1)

name = sys.argv[1]

if os.path.exists(name):
    print("오류: '" + name + "' 폴더가 이미 존재합니다.")
    sys.exit(1)

os.makedirs(name + "/data")
os.makedirs(name + "/doc")
os.makedirs(name + "/src")

with open(name + "/doc/README", "w") as f:
    f.write("프로젝트: " + name + "\n")

print(name + " 프로젝트를 만들었습니다.")