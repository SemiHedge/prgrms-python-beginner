# n, n-1, n-2, ... 1 또는 0까지
# 재귀함수(Recursion)

def countdown(number):
    print(number)
    if number == 0:
        return
    else:
        countdown(number-1)


countdown(10)


