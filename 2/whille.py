customer = "유정민"
index = 5
while index >= 1 :
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer,index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")

"""
index = 1
while True :  # 무한루프
    print("{0},커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
    index += 1
"""
person = "Unknown"
while person != customer :
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")  # 손님이 주문자에 맞을때까지 반복