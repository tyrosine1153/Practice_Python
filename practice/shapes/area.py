# 도형의 넓이를 구하는 함수
PI = 3.14


def circle(radius):
    return PI * radius * radius


def square(length):
    return length * length

if __name__ == '__main__':
    print("area에서 실행됨")
# 스크립트처럼 쓴 파일을 다른 파일에서 모듈로 임포트 하면 임포트한 파일의 스크립트가 실행된다


# __name__ : 모듈의 이름을 저장해놓은 변수.
# __main__ : 실행되는 스크립트의 이름

print(f"area의 모듈 이름 : {__name__}")
# run 에서 실행 : "area의 모듈 이름 : practice.area.area"
# area 에서 실행 : "area의 모듈 이름 : __main__"