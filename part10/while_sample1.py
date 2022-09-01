# 2가 몇 번 곱해져야 1000만이 넘을까?
# 몇 번에 대한 것이 미지수, 무한반복의 가능성 -> while
# 처리할 데이터가 정해져 있거나, 최대 몇 번에 대한 것이 정해짐, 무한반복은 X -> for
goal_num = 10000000
step = 2
result = 1

count = 0
while result < goal_num:
    result *= step
    count += 1
print(f'count:{count} result:{result}')

