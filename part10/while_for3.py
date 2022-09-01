# while vs for
# while은 값에 따라 반복 여부를 정할 수 있다.
# 못 찾는다면 무한하게
goal_num = 10000000
step = 2
result = 1

count = 0
while result < goal_num:
    result *= step
    count += 1
print(f'count:{count} result:{result}')

# for는 정해진 횟수, 데이터 개수처럼 한계치가 정해진 상황
# 때문에 limit를 준 상황으로 반복
goal_num = 10000000
step = 2
result = 1

count = 0
for n in range(25):  # 최대 25번 곱하기
    result *= 2
    count += 1
    if result >= goal_num:
        print(f'count:{count} result:{result}')
        break
