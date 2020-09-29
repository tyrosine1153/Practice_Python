def profile(name, age, main_lang):
    print("이름 : {0} \t나이 : {1}\t주 사용 언어 : {2}" \
          .format(name, age, main_lang))


profile("유정민", 17, "C")
profile("이종은", 17, "Java")


# 같은 나이의 경우, 디폴트
def _profile(name, main_lang, age=17):  # 디폴트값은 맨 마지막에만 지정할수있음
    print("이름 : {0} \t나이 : {1}\t주 사용 언어 : {2}" \
          .format(name, age, main_lang))


_profile("유정민", "C")
_profile("이종은", "Java")


# 키워드
def __profile(name, age, main_lang):
    print(name, age, main_lang)


profile(name="유정민", main_lang="C", age=17)  # 순서가 뒤섞여도 전달됨
profile(main_lang="Java", age=17, name="이종은")


# 가변인자
def ___profile(name, age, *language):  # language 이거
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    # end=" " : 이 함수가 끝날때 줄바꿈을 하지 않음
    for lang in language:
        print(lang, end=" ")
    print()

___profile("김선민", 18, "C", "C#", "C++", "Java", "Python")
___profile("유정민", 17, "C")  # 변수가 적거나 너무 맞으면 귀찮음