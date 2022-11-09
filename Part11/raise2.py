# 삼각형 넓이 Define Function  + raise
def calc_triangle(width, height):
    if width < 0 or height < 0:
        raise ValueError("Negative numbers are not allowed.")
    area = width * height / 2
    return area


# 함수 실행
t1 = calc_triangle(10, 20)
t2 = calc_triangle(100, 200)
print(t1+t2)
t3 = calc_triangle(-100, -200)