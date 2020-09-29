# 집합 (set)
# 중복 안 됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)  # 1, 2, 3만 출력 됨

jung_byung = {"이찬명", "홍단", "유정민"}
unjung_byung = set(["유정민", "이찬명"])

print(jung_byung & unjung_byung)  # 교집합 출력
print(jung_byung.intersection(unjung_byung))

print(jung_byung | unjung_byung)  # 합집합 출력
print(jung_byung.union(unjung_byung))

print(jung_byung - unjung_byung)  # 차집합 (정병이지만 un 정병이 아닌사람)
print(jung_byung.difference(unjung_byung))

jung_byung.add("유정민")  # 정병집합에 유정민 추가
print(jung_byung)

jung_byung.remove("유정민")  # 정병집합에 유정민 삭제
print(jung_byung)