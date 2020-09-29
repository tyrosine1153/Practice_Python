class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 4일] 방콕, 파타야 여행 (야시장 투어) 50만원")

# 모듈이 잘 돌아가는지 실행함. 모듈 직접 실행
if __name__ == "__name__":  # 이파일에서 실행할때
    print("Thailand 모듈 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요.")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")  # 다른 파일에서 모듈을 실행할때 호출됨