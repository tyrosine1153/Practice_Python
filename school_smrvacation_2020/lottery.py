from random import *
from time import *

num = int(int(input("복권을 얼마어치 사실거에요??(천원이상): "))/1000)
print(strftime("%Y-%m-%d"))
print("로또 추첨번호")
list = []
for i in range(num):
    list = [randint(1, 45) for j in range(6)]
    list.sort()
    print(f"{i+1}. {list}")