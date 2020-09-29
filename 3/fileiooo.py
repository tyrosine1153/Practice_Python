score_file = open("score.txt", "w", encoding="utf8")
# 파일 이름, 모드, 문자해석. "w": 쓰기 목적. 덮어쓰기
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8")
# "a": 쓰기 목적, 뒤에
score_file.write("과학 : 80")
score_file.write("\n국어 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
# "r": 읽기 목적
print(score_file.read(), "\n")
# 파일에서 읽은 것을 모두 출력
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())  # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")  # 줄바꿈 안함
score_file.close()

print("")

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()
# 몇줄인지 모를때 줄 끝까지 스캔해서 출력하는 것

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
# 이것도 전체 스캔해 출력하는 방법
