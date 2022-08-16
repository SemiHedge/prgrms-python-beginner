# int_convert_str.py
year = 2020
month = 12
day = 25
birth = year + month + day
print(birth)

year = '2020'
month = '12'
day = '25'
birth = year + month + day
print(birth)

year = str(2020)  # '2020'
month = str(12)  # '12'
day = str(25)  # '25'
birth = year + month + day
print(birth)

# str(v) string
# int(v) integer
num1 = int(3.0)
print(num1)
num2 = float(3)
print(num2)
# num3 = int("가나다")  # ValueError
# print(num3)
num4 = int("3.0")  # ValueError
print(num4)