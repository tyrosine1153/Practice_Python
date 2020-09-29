print("나는 %d살 입니다" % 17)
print("나는 %s을 싫어해요" % "파이썬")
print("Apple은 %c로 시작합니다" % 'A')

print("나는 {}살 입니다".format(17))
print("나는 {}과 {}을 좋아해요".format("파란색", "흰색"))
print("나는 {0}과 {1}을 좋아해요".format("파란색", "흰색"))
print("나는 {1}과 {0}을 좋아해요".format("파란색", "흰색"))

print("나는 {age}살이며, {color}을 좋아해요".format(age=17, color="파란색"))
print("나는 {age}살이며, {color}을 좋아해요".format(color="파란색", age=17))

age = 17
color = "파란색"
print(f"나는 {age}살이며, {color}을 좋아합니다.")
# \r : 커서 맨 앞으로 이동 / \d : 백스페이스

'''ex = "http://naver.com"
ex = ex.replace("http://", "")  # http://제외
ex = ex[:ex.find(".")]  # .이후 없앰
ex = ex[:3] + str(len(ex)) + str(ex.count("e")) + "!"
#남은 문자열중 세자리, 글자갯수, 글자 내 'e' 개수, "!"의 합성
print(ex)'''