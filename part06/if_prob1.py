# 짝수, 홀수
number = int(input("정수 입력 : "))

# 짝수 홀수를 구분하는 if문을 작성하세요
if number % 2:
    print(f'{number} > 홀수')
else:
    print(f'{number} > 짝수')