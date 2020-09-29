# 모듈: 같은 용도로 계속해서 선언해 쓰는 클래스와 함수를 따로 빼내 부품처럼 쓰는 것
import theater_module
theater_module.price(3)  # 세 명의 일반요금을 냈을때
theater_module.price_morning(4)
theater_module.price_soldier(5)

import theater_module as mv  # 별명으로 줄여서 쓸 수 있다
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *  # 아예 전부를 생략해 쓸 수 있다
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning  # 일부만 생략해 쓸 수 있다
price(3)
price_morning(4)
theater_module.price_soldier(5)

from theater_module import price_soldier as price
# price_soldier 만 theater_module 을 생략해 쓰면서 동시에 price_soldier 을 price 로 바꿔 부름
price(5)  # 아까 썼던 price_soldier(5)과 같음
