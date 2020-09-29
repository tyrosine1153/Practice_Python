for waiting_num in [0, 1, 2, 3, 4]:
    # for(int waiting_num = 0; waiting_num < modulee; waiting_num++)
    print("대기번호 : {}".format(waiting_num))

for waiting_num in range(5):  # 0, 1, 2, 3, 4
    print("대기번호 : {}".format(waiting_num))

for waiting_num in range(1, 6):  # 1, 2, 3, 4, modulee
    print("대기번호 : {}".format(waiting_num))

cafe = ["가영", "나영", "다영"]
for customer in cafe:
    print("{}님, 커피가 나왔습니다".format(cafe))

# 한 줄 for 문
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104, 105
students = [1, 2, 3, 4, 5]
print(students)
students = [i + 100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["유정민", "이찬명", "홍태희", "김선민"]
students = [len(i) for i in students]
print(students)

# 힉생 이름을 대문자로 변환
students = ["jungmin", "chanmyeong", "sunmin"]
students = [i.upper() for i in students]
print(students)