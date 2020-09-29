gun = 10


def checkPoint(soldiers):
    global gun  # 전역공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


def checkPoint_ret(gun, soldiers):  # 함수 내에서만 쓸 수 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkPoint(2)  # 2명이 근무로 총을 가져감
gun = checkPoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))







