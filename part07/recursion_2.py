# 팩토리얼
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)


# 테스트
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))