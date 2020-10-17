PI = 3.14

from mymath.shapes import area, volume

# 패키지를 임포트 할때 패키지 안에 있는 내용도 함께 임포트 하기 위해 임포트 하고 싶은 것들을 쓴다
print("__init__.py 파일 실행")  # 패키지가 임포트될때 제일 먼저 실행되는 파일

__all__ = ['area', 'volume', 'shapes2d']  # import * 를 했을때 불러와야 할 모듈의 모음
# __all__ 을 사용했을 때 from ~ import * 에서 어떤 모듈이 임포트되는지 제어할 수 있음
# __init__.py가 아니라도 다른 파일에서도 지정 가능
