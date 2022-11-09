# raise
# raise KeyboardInterrupt
# raise ZeroDivisionError

# 값을 음수로 받을 경우 ValueError
# number = int(input("Test Number : "))
# if number < 0:
#     raise ValueError("Negative numbers are not allowed.")

# 오류 생성 + 제어
try:
    number = int(input("Test Number : "))
    if number < 0:
        raise ValueError("Negative numbers are not allowed.")
except ValueError as ve:
    print(ve)