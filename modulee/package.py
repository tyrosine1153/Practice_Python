# 여러 모듈 파일들을 모아놓은 것
import travel.thailand  # 클래스나 함수단위 까지는 임포트까지 할 수 없음. 모듈까지만 가능
trip_to = travel.thailand.ThailandPackage()  # 패키지.모듈.클래스
trip_to.detail()  # (패키지.모듈.클래스).함수

from travel.thailand import ThailandPackage  # 클래스로만 줄여서 쓸 수 있다
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from travel import *  # 이렇게 해도 그냥은 패키지안의 모든 범위는 포함되지 않음 __init__안에서 설정해야함
trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()

import inspect
import random
print(inspect.getfile(random))  # 모듈 파일이 어디 있는지 알려줌
print(inspect.getfile(thailand))