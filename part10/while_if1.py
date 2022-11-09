# while 조건 > while True if break
# while 조건식
goal_num = 10000000
step = 2
result = 1

count = 0
while result < goal_num:
    result *= step
    count += 1
print(f'count:{count} result:{result}')


# while True:
goal_num = 10000000
step = 2
result = 1

count = 0
while True:
    result *= step
    count += 1
    if result >= goal_num:
        break
print(f'count:{count} result:{result}')