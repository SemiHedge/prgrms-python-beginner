import math
nums = [1, 99, 2, 3, 4]
print(sum(nums))
print(max(nums))
print(min(nums))

print(abs(-5))
print(abs(5))

# divisor + modulo
# 몫 : quotient, 나머지 : remainder
q, r = divmod(5, 3)
print(q, r)

print(math.factorial(3))
print(math.factorial(4))
print(math.factorial(5))

# 루트
print(math.sqrt(2))
print(math.sqrt(3))
print(math.sqrt(4))

# 로그함수
print(math.e)
print(math.log2(2))
print(math.log10(10**2))
print(math.log(math.e))  # 자연로그 e
print(math.log(49, 7))  # log7

# 삼각함수
print(math.pi)
print(math.sin(math.radians(30)))
print(math.sin(math.radians(45)))
print(math.sin(math.radians(60)))

# 반올림 - ROUND
print(math.ceil(3.14))
print(math.floor(3.14))
print(math.floor(-3.14))
print(math.floor(3.14))
print(math.floor(-3.14))
