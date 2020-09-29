# 내장함수 : 따로 임포트할 필요 없이 바로 사용 가능한 함수
# ex) input, dir...

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 사용할 수 있는지 표시
print(dir())
import random
print(dir())  # 랜덤이 추가됬다

print(dir(random))  # 랜덤모듈에서 쓸 수 있는 함수, 변수 표시
list = [1, 2, 3]
print(dir(list))  # list. 했을때 자동완성으로 뜨는 내용들이 대게 나옴
name = "Jim"
print(dir(name))  # name. 했을때 자동완성으로 뜨는 내용들이 대게나옴

# 여기서 파이썬의 내장함수를 볼 수 있음
# https://docs.python.org/ko/3/library/functions.html#built-in-functions


# 외장함수 : 모듈로 임포트해서 쓸 수 있는 함수
# 여기서 파이썬의 모듈들을 볼 수 있음
# https://docs.python.org/3/py-modindex.html

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py"))  # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())  # 현재 디렉토리 표시

folder = "sample_dir"

# 현재 어떤 계정으로 로그인 돼있는지 확인
print(os.getlogin())

# 현재 파일의 디렉토리 확인
print(os.getcwd())

# 현재 프로세스 ID 확인
print(os.getpid())

if os.path.exists(folder):  # 같은 경로에 같은 이름의 폴더가 있는지 확인
    print("이미 존재하는 폴더입니다")
    os.rmdir(folder)  # 이 이름의 폴더를 삭제
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)  # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir())  # glob 과 비슷함

import time  # 시간 관련 함수 제공
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()  # 오늘 날짜 저장
td = datetime.timedelta(days=100)  # 100일 저장
print("우리가 만난지 100일은", today + td)


# 현재 시간과 날짜
today = datetime.datetime.now()
print(today)

# 출력값을 "요일, 월 일 연도"로 포매팅
print(today.strftime("%A, %B %dth %Y"))

# 특정 시간과 날짜
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)

# 두 datetime의 차이
print(today - pi_day)

