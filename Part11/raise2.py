# raise KeyboardInterrupt
# raise ValueError

# 값을 음수로 받을 경우 ValueError를 띄워보자
def calc_triangle(width, height):
    if not (width > 0 and height > 0):
        raise ValueError("Negative numbers are not allowed.")
    return width * height / 2

tr1 = calc_triangle(3, 4)
tr2 = calc_triangle(30, 40)
print(tr1, tr2)
tr3 = calc_triangle(-30, 40)  # ValueError

# 만일 마땅한 예외 유형이 없다면, 거의 모든 예외 상황의 부모였던 Exception을 쓰자.
# raise Exception
def calc_triangle(width, height):
    if not (width > 0 and height > 0):
        raise Exception("Negative numbers are not allowed.")
    return width * height / 2

tr1 = calc_triangle(3, 4)
tr2 = calc_triangle(30, 40)
print(tr1, tr2)
tr3 = calc_triangle(-30, 40)  # Exception