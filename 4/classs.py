class Unit:  # 일반 유닛
    def __init__(self, name, hp, speed):
        self.name = name  # 맴버 변수
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
              .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


class Flyable:  # 날 수 있는 기능을 가진 클래스
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
              .format(name, location, self.flying_speed))


class AttackUnit(Unit):  # 공격 유닛, (Unit)유닛을 상속
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)  # 부모 클래스의 초기화 함수를 받아 씀
        self.damage = damage

    def attack(self, location):  # 메소드
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name, location, self.damage))


class FlyableAttackUnit(Flyable, AttackUnit):  # 공중 공격 유닛. 다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 스피드는 받지 않음
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
        # 지상유닛이 사용하는 함수와 비슷해 사용하기 쉬움. 재정의, 메소드 오버라이딩


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        # super: 위에 것 대신쓸 수 있음. 다중 상속의 경우 슈퍼를 쓰면 하나의 클래스만 상속됨
        self.location = location
        pass  # 다 완성 안해도 일단 완성한 것 처럼 처리


def game_start():
    print("[알림] 새로우 게임을 시작합니다.")


def game_over():
    pass

# self : 자기 자신을 의미함. 자기 자신에 접근할때 이용함
# __init__: 생성자, 마린1,2 탱크를 처음 만들때 호출되는 것
# 클래스로부터 만들어 지는 것들의 개념 객체 / 각각을 인스턴스라고 부름
marine1 = AttackUnit("마린", 40, 5, 5)
tank1 = AttackUnit("탱크", 150, 35, 5)
wraith1 = AttackUnit("레이스", 80, 5, 5)
wraith2 = AttackUnit("레이스", 80, 5, 5)
wraith2.clocking = True  # 멤버 확장 가능
firebat1 = AttackUnit("파이어뱃", 50, 16, 5)
valkyrie1 = FlyableAttackUnit("발키리", 200, 6, 5)
vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
# 객체.멤버 형식으로 변수같이 쓸 수 있음

if wraith2.clocking:  # == True 가 생략됨
    print("{0}은 현재 클로킹 상태입니다.".format(wraith2.name))
# if wraith1.clocking == True:  # 확장한다고 한 wraith 이 아니면 확장한 멤버를 사용할 수었음
#     print("{0}은 현재 클로킹 상태입니다.".format(wraith2.name))

firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)
valkyrie1.fly(valkyrie1.name, "3시")
vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "11시")
battlecruiser.move("11시")
