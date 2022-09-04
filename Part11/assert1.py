# raise KeyboardInterrupt
# raise ValueError

# 값을 음수로 받을 경우 ValueError를 띄워보자
def calc_triangle(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Negative numbers are not allowed.")
    return width * height / 2

def calc_triangle(width, height):
    assert width > 0 and height > 0, "Negative numbers are not allowed."
    assert type(width) is int, 'Allow integer'
    assert type(height) is int, 'Allow integer'
    return width * height / 2

tr1 = calc_triangle(3.1, 4)
tr2 = calc_triangle(30, 40)
print(tr1, tr2)
tr3 = calc_triangle(-30, 40)  # ValueError
tr4 = calc_triangle(30, 40)
