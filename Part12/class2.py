# class1을 참고한 클래스 User 생성 -> Python tutor로 확인
class User:
    def __init__(self, name):
        self.name = name  # Ctrl(Cmd) + D or Ctrl(Cmd) + Shift + L
        self.energy = 50
        self.level = 1

    def show(self):
        print(f'STAT : name:{self.name}  energy:{self.energy}  level:{self.level} ')

    def eat(self, food):
        if food == '이상한사탕':
            self.energy += 100
        elif food in ['빵', '김밥', '라면']:
            self.energy += 30
        else:
            self.energy += 10

    def level_up(self):
        if self.energy < 100:
            print(f"실패 : 에너지 100 필요 - energy:{self.energy}")
            # raias ValueError(f"에너지가 부족 - energy:{self.energy}")
        else:
            self.energy -= 100
            self.level += 1
            print(f"레벨 업 : energy:{self.energy}  level:{self.level}")


# 메인 영역
player1 = User('Spencer')
player1.show()
player1.eat('빵')
player1.level_up()
player1.eat('이상한사탕')
player1.level_up()
player1.eat('이상한사탕')
player1.level_up()

player2 = User('Mussg')
player2.eat('이상한사탕')
player2.level_up()
player2.eat('이상한사탕')
player2.level_up()

player1.show()
player2.show()