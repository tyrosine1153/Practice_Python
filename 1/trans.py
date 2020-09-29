# 자료구조의 변경
"""
menu = {"커피", "우유", "주스"}  # 집합 (set)
print(menu, type(menu))

menu = list(menu)  # 목록으로 변환
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
"""
from random import *
list1 = [1, 2, 3, 4, 5]
shuffle(list1)  # 목록에 있는거 무작위로 섞음
print(sample(list1, 2))  # 리스트에 있는 2개를 무작위로 뽑음

list2 = range(1, 21)  # 1 ~ 20의 숫자
list2 = list(list2)  # 자료형 range->list
shuffle(list2)

winners = sample(list2, 4)
print("--당첨자 발표--")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print("--축하합니다--")