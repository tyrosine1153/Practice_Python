from practice.area import area as ar
from practice.area import shapes2d as sh
from practice.area.shapes2d import Square as Sq

print(ar.circle(2))
print(ar.square(3))
print(ar.PI)


circle = sh.Circle(2)  # 생성자
print(circle.area())


square = Sq(3)  # 생성자
print(square.area())

# namespace: 파일에서 정의된 모든 이름들 -> dir() namespace 를 알려주는 함수

print(dir(ar))
# dir(area): area 파일의 네임스페이스를 알려주는 함수
# PI, circle, square 과 던더(double under score)라고 읽는 특수변수들이 있다
# 특수변수: 파이썬이 내부적으로 관리하는 변수들

print(dir())
# dir(): 현재 파일의 네임스페이스를 알려주는 함수
# 임포트한 모듈도 있다. 모듈안에서 정의된 것은 나오지 않음
# 임포트 방식, 생성자에 따라 파일에 정의 되는 이름이 다르다

# 파이썬에서는 같은 이름의 함수가 정의 되었을때

