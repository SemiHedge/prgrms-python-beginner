# type() 함수로 봤던 class
name = 'Spencer'
energy = 50
level = 1

def show():
    print(f'STAT : name:{name}  energy:{energy}  level:{level} ')

def eat(food):
    global energy  # 설명을 위해 임시
    if food == '이상한사탕':
        energy += 100
    elif food in ['빵', '김밥', '라면']:
        energy += 30
    else:
        energy += 10

def level_up():
    global energy, level   # 설명을 위해 임시
    if energy < 100:
        print(f"실패 : 에너지 100 필요 - energy:{energy}")
        # raias ValueError(f"에너지가 부족 - energy:{energy}")
    else:
        energy -= 100
        level += 1
        print(f"레벨 업 : energy:{energy}  level:{level}")


# 메인 영역
show()
eat('빵')
level_up()
eat('이상한사탕')
level_up()
eat('이상한사탕')
level_up()