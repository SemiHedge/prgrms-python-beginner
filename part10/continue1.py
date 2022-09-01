# continue
for n in range(1, 30):
    if n % 3 == 0:
        break  # 현 시점에 반복문 종료
    print(n)

print('='*10)

for n in range(1, 30):
    if n % 3 == 0:
        continue  # 이번 차례 SKIP. 현 시점에서 다음 차례 반복으로 넘어감
    print(n)

# while 
n = 0
end = 30
while n < end:
    n += 1
    print(n)
    if n % 3 == 0:
        continue

# 이건 안 끝남 - 무한반복
n = 1
end = 30
while n < end:
    print(n)
    if n % 3 == 0:
        continue
    n += 1

# 문법 학습을 위한 예제이지, 유의미해 보이진 않는다.
# 2번째 예제를 해보자.