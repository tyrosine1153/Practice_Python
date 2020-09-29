# 프로그램에서 사용하는 데이터를 파일로 저장하는 것
import pickle
profile_file = open("profile.pickle", "wb")  # "wb"쓰기목적 바이너리, encoding 설정은 필요하지 않음
profile = {"이름": "유정민", "나이": 17, "취미": ["게임", "코딩", "윗 사람한테 개기기"]}
print(profile)
pickle.dump(profile, profile_file)  # 피클을 이용해 데이터를 파일에 씀
profile_file.close()

profile_file = open("profile.pickle", "rb")  # "rb"읽기 목적 바이너리
profile = pickle.load(profile_file)
print(profile)
profile_file.close()


# with : 파일을 열고닫고 처리를 하는 것을 간단하게 함

# import pickle
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
# 자동으로 닫아줌

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 좆같이 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())



