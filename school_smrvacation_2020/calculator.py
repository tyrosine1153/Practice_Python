def plus(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1, num2


def multi(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2

if __name__ == "__main__":
    print("모듈 파일에서 실행")
else:
    print("다른 파일에서 임포트되어 실행")