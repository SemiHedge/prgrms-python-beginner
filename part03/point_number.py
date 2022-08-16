# floating_point_number expression
num1 = 123.456789

# round() -> 숫자
num2 = round(num1, -1)
print(num2)

# format() -> 문자열
num2 = "{:.2f}".format(num1)
print(num2)  # str -> int float 형변환

# fstring -> 문자열
num2 = f"{num1:.2f}"
print(num2)
