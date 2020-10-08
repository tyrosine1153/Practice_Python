from random import *

answer = randint(1, 100)

num = int(input("숫자를 입력하세요. "))

while num != answer:
    if num < answer:
        print("숫자가 작습니다.")
    else:
        print("숫자가 큽니다")
    num = int(input("숫자를 입력하세요. "))
print(f"{answer} 정답입니다!")