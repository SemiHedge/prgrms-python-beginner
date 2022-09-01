# raise KeyboardInterrupt
# raise ValueError

# 값을 음수로 받을 경우 ValueError를 띄워보자
number = int(input("Test Number : "))
if number < 0:
    raise ValueError("Negative numbers are not allowed.")


try:
    number = int(input("Test Number : "))
    if number < 0:
        raise ValueError("Negative numbers are not allowed.")
except ValueError as ve:
    print(ve)
