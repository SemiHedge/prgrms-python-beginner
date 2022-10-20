n = int(input("숫자를 입력하세요 : "))
print(f'구구단 {n}단')
for i in range(1, 10):
    print(f'{n} * {i} = {n * i}')