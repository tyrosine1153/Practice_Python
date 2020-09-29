print("Python", "Java")
print("Python", "Java", sep=",")  # 변수 사이의 문자열을 sep 으로 지정할 수 있음
print("Python", "Java", end="?\n")  # 문장의 끝부분에 올 문자열을 지정할 수 있음

import sys
print("Python", "Java", file=sys.stdout)  # 표준출력
print("python", "Java", file=sys.stderr)  # 표준에러. 에러로 표시됨

score = {"수학": 0, "영어": 50, "국어": 100}
for subject, score in score.items():
    print(subject.ljust(5), str(score).ljust(4), sep=":")
    # .ljust에 쓴 만큼 띄어쓰기

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
    # .zfill에 쓴만큼 0으로 채우기

print("{0: >20}".format("Hello world"))
# 빈자리는 빈 공간으로 두고 20자리를 확보하며, 오른쪽 정렬을 함(>)
print("{0:_<20}".format("Hello world"))
# 왼쪽 정렬하고 빈칸을 _로 채움

print("{0: >+20}".format(500))
print("{0: >+20}".format(-500))
# 양수일떈 +로 표시, 음수일땐 -로 표시

print("{0:,}".format(10_000_000_000))
# 세 자리마다 콤마 찍어주기
print("{0:+,}".format(10_000_000_000))
print("{0:+,}".format(-10_000_000_000))
# 위에것도 응용가능

print("{0:^<+20,}".format(10_000_000_000))
# 빈곳은 ^로 찍고, 왼쪽으로 정렬하며, 부호를 표시하고, 20개의 자릿수를 표시하고, 세자리마다 콤마붙임
# 출력: +10,000,000,000^^^^^
print("{0:.2f}".format(5/3))
# 소수점 출력, 특정 자리수 까지만 표시(소수점 3째 자리에서 반올림)