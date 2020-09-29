# 사용자 정의 예외처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

# 예외처리
try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("피제수를 입력하세요. :  "))
    num2 = int(input("제수를 입력하세요. :  "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하셨습니다.")
except ZeroDivisionError as err:  # 이유가 명확한 에러의 경우에 대해 처리하는 것
    print(err)
except:  # 나머지 에러를 표시할때
    print("알 수 없는 에러가 발생했습니다.")
"""  # 이렇게도 할 수 있음
except Exception as err:
    print(err)
"""
# 에러 만들기
try:
    print("한 자리 숫자 나누기 전용 계산기 입니다")
    num1 = int(input("피제수를 입력하세요. :  "))
    num2 = int(input("제수를 입력하세요 :  "))
    if num1 >= 10 or num2 >= 10:
        # raise ValueError
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))  # 메세지로 전달할 말
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:  # 예외가 나건 나지 않건 무조건 실행되는 구문. try 에서 제일 마지막으로 실행됨
    print("계산기를 이용해 주셔서 감사합니다")