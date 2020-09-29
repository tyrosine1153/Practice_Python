menu = ("돈까쓰", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스")  #오류: 튜플은 수정 추가가 안 됨
"""
name = "유정민"
age = 17
hobby = "윗사람한테 개기기"
print(name, 17, hobby)
"""
(name, age, hobby) = ("유정민", 17, "윗사람한테 개기기")
print(name, 17, hobby)  # 위에 거랑 의미가 같다

name = "이찬명"
print(name)