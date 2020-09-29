id_number = "040406-4358313"

print("주민번호 : " + id_number)
print("성별 : " + id_number[7])
print("생년월일 : " + id_number[:6])
print("연 : " + id_number[0:2])
print("월 : " + id_number[2:4])
print("일 : " + id_number[4:6])

print("앞 6자리 : " + id_number[:6])
print("뒤 7자리 : " + id_number[7:])
print("뒤 7자리 : " + id_number[-7:])  # 뒤 7자리부터