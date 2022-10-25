# while
numbers = [-3, 3, 6, -6, 4, 6, 8, 1, 0, 2, 0, -5]
print(f'기존 numbers : {numbers}')

# 마이너스(-)는 모두 플러스(+)로 변환시킨다
index = 0
while index < len(numbers):
    if numbers[index] < 0:
        numbers[index] *= -1 
    index += 1
print(f'변경 numbers : {numbers}')