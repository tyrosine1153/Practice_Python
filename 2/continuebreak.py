"""
absent = [2, modulee]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue  # 밑의 문장 무시
    elif student in no_book:
        print("오늘 수업은 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐.".format(student))
"""
from random import *

count = 0
for guest in range(1, 51):
    time = randint(5, 50)
    if time <= 15:
        count += 1
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(guest, time))
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(guest, time))
print("총 탑승 승객 : {0} 분".format(count))