import os.path  # 파일 경로를 다룸

# 프로젝트 디렉토리 경로 '/Users/codeit/PycharmProjects/standard_modules'
# 현재 파일 경로 '/Users/codeit/PycharmProjects/standard_modules/main.py'

# 주어진 경로를 절대 경로로
print(os.path.abspath('..'))

# 주어진 경로를 현재 디렉토리를 기준으로 한 상대 경로로
print(os.path.relpath('/Users/codeit/PycharmProjects'))

# 주어진 경로들을 병합
print(os.path.join('/Users/codeit/PycharmProjects', 'standard_modules'))
''' 실행결과
/Users/codeit/PycharmProjects
..
/Users/codeit/PycharmProjects/standard_modules'''

import re  # Regular Expression(정규 표현식) : 특정한 규칙/패턴을 가진 문자열을 표현하는 데 사용

# 알파벳으로 구성된 단어들만 매칭
pattern = re.compile('^[A-Za-z]+$')
print(pattern.match('I'))  # <re.Match object; span=(0, 1), match='I'>
print(pattern.match('love'))  # <re.Match object; span=(0, 4), match='love'>
print(pattern.match('python3'))  # None

print()

# 숫자가 포함된 단어들만 매칭
pattern = re.compile('.*\d+')
print(pattern.match('I'))  # None
print(pattern.match('love'))  # None
print(pattern.match('python3'))  # <re.Match object; span=(0, 7), match='python3'>

import pickle  # 파이썬 오브젝트를 바이트 형식으로 바꿔서 파일에 저장하고 읽어옴

# 딕셔너리 오브젝트
obj = {'my': 'dictionary'}

# obj를 filename.pickle 파일에 저장
with open('filename.pickle', 'wb') as f:
    pickle.dump(obj, f)

# filename.pickle에 있는 오브젝트를 읽어옴
with open('filename.pickle', 'rb') as f:
    obj = pickle.load(f)

print(obj)

import json  # 오브젝트를 json 형식으로 바꿔줌.
# json 형식에 맞는 기본 데이터 타입, 리스트, 딕셔너리만 바꿀 수 있음

# 딕셔너리 오브젝트
obj = {'my': 'dictionary'}

# obj를 filename.json 파일에 저장
with open('filename1.json', 'w') as f:
    json.dump(obj, f)

# filename.json에 있는 오브젝트를 읽어옴
with open('filename1.json', 'r') as f:
    obj = json.load(f)

print(obj)

import copy  # 파이썬 오브젝트를 복사할 때 쓰임

# '=' 연산자는 실제로 리스트를 복사하지 않음.
# 리스트를 복사하려면 슬라이싱을 사용하거나 copy.copy() 함수를 사용해야 함
a = [1, 2, 3]
b = a
c = a[:]
d = copy.copy(a)
a[0] = 4
print(a, b, c, d)
# [4, 2, 3] [4, 2, 3] [1, 2, 3] [1, 2, 3] b 는 a 를 참조하지만 c, d 는 a를 복사함

# 하지만 오브젝트 안에 오브젝트가 있는 경우 copy.copy() 함수는 가장 바깥에 있는 오브젝트만 복사함
# 오브젝트를 재귀적으로 복사하려면 copy.deepcopy() 함수를 사용해야 함
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = copy.copy(a)
c = copy.deepcopy(a)
a[0][0] = 4
print(a, b, c)
# [[4, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[4, 2, 3], [4, 5, 6], [7, 8, 9]] b는 a의 가장 바깥 오브젝트만 복사함
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]] c는 a를 전부 복사함

"""
import sqlite3  # SQLite 데이터 베이스 사용

# 데이터베이스 연결
conn = sqlite3.connect('example.db')

# SQL 문 실행 
c = conn.cursor()
c.execute('''SELECT ... FROM ... WHERE ... ''')

# 가져온 데이터를 파이썬에서 사용
rows = c.fetchall()
for row in rows:
    print(row)

# 연결 종료
conn.close()
"""