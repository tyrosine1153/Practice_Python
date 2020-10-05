from random import *

right = randint(1,20)

chance = 5
while chance:
    answer = int(input(f"기회가 {chance}번 남았습니다. 1-20사이의 숫자를 맞혀보세요: "))
    chance -= 1
    if answer < right:
        print("UP")
    elif answer > right:
        print("DOWN")
    else:
        print(f"축하합니다. {5-chance}번 만에 숫자를 맞히셨습니다.")
        break

if chance == 0:
    print(f"아쉽습니다. 정답은 {right}입니다.")