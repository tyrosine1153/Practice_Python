python = "Python is Amazing"

print(python.lower())  # 소문자
print(python.upper())  # 대문자
print(python[0].isupper())  # 대문자 확인
print(len(python))  # 글자 수 (공백포함)
print(python.replace("Python", "CLang"))  # 첫번째 문자열이 있는 위치를 찾아 두번째 문자열로 바꿈

index = python.index("n")
print(index)  # n 이 있는 첫번째 위치
index = python.index("n", index + 1)
print(index)  # n 이 있는 두번째 위치

print(python.find("Clang"))  # 아까와 비슷하지만 찾는 문자열이 없으면 -1반환
# print(python.index("CLang"))  # 찾는 문자열이 없으면 오류

print(python.count("n"))  # 문자열이 들어간 개수