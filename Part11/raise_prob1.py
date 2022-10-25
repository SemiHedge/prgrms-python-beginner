# 값을 음수로 받을 경우 ValueError를 띄워보자
number = int(input("Test Number : "))
try:
    if number < 0:
        raise
except:
    print("오류 발생")