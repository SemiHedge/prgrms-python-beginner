출력 = print
# param_func2.py
# 삼각형 넓이 Define Function 
def calc_triangle(width, height):
    # area = width * height / 2
    # return area
    return width * height / 2

# 함수 실행
t1 = calc_triangle(10, 20)
print(t1)

# 변수에 함수 저장
new_func = calc_triangle
t1 = new_func(10, 20)
print(t1)


# lambda로 익명함수 구현
# lambda 매개변수 : 식
lambda_func = lambda width, height : width * height / 2
t1 = lambda_func(10, 20)
print(t1)

# 람다로 만든 함수는 다른가?
print(calc_triangle)
print(new_func)
print(lambda_func)  # <function <lambda> at 0x0000000000000000>

# 이것만으론 lambda 장점을 알기 어렵다.
# 리턴 값도 한 줄로만 작성해야되고...
# lambda는 다른 문법과 합쳐졌을 때 장점이 있다. 다른 것을 빛을 내게 함.