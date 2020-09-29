subway = ["코끼리", "토끼", "호랑이"]
print(subway)

print(subway.index("토끼"))  # 토끼의 순서

subway.append("고양이")  # 맨 뒤에 새로운 문자열 추가
print(subway)

subway.insert(1, "강아지")  # 1번째와 그 다음 사이에 새로운 문자열 추가
print(subway)

print(subway.pop())  # 맨 뒤에서 하나를 없애고 없앤 것을 출력한다
print(subway)  # 다음 출력해보면 뒤에가 없어진걸 알 수 있음

subway.append("코끼리")
print(subway)
print(subway.count("코끼리"))  # 코끼리의 수


num_list = [5, 4, 8, 6, 3]
num_list.sort()  # 오름차순 정렬
print(num_list)

num_list.reverse()  # 내림차순 정렬
print(num_list)

mix_list = ["유정민", 17, True]
# num_list += mix_list  # 리스트 합치기
num_list.extend(mix_list)  # 리스트 합치기
print(num_list)