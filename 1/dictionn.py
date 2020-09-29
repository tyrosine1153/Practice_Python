# key, value 로 구성. key 의 중복이 안됨
cabinet = {0: "유정민", 5: "이찬명", 6: "심준호", 10: "고경태"}

print(cabinet[0])
print(cabinet.get(5))

# print(cabinet[3])  # 사전에 없는 key 면 오류가 남
# print(cabinet.get(3))  # 사전에 없는 key 면 None 이 출력 됨
print(cabinet.get(3, "key 없음"))  # 사전에 없는 key 면 문자열이 출력 됨

print(3 in cabinet)  # 3 이 cabinet 에 있는 key 인지 판단 (T/F)
print(5 in cabinet)

cabinet = {"A-0": "유정민", "B-5": "이찬명"}
print(cabinet)
print(cabinet["A-0"])

cabinet["C-6"] = "심준호"  # 새로운 키 추가
cabinet["A-0"] = "고경태"  # 원래 키에 새로운 항목 대체
print(cabinet)

del cabinet["B-5"]  # 키 삭제
print(cabinet)

print(cabinet.keys())  # key 들만 출력
print(cabinet.values())  # value 들만 출력
print(cabinet.items())  # 둘다 출력

cabinet.clear()  # 다 없애기
print(cabinet)