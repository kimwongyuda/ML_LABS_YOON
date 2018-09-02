"""
해시:
1. 해시 테이블: 딕셔너리, 객체
2. 정해진 길이의 문자열
"""

import hashlib

with open("tower.jpg", "rb") as file:
    string = file.read()
    print(string)