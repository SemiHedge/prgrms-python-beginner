# 이미 살펴본 파라미터 기본값 지정
# print(*values, sep='', end='\n')

def teleport(x=0, y=0, z=1):
    print(f'텔레포트 {x},{y},{z}')

teleport(10, 10, 10)
teleport(10, 10)
teleport(10)
teleport() 

# 위치 에너지 mgh 지구:9.807m/s² 화성:3.721m/s² 달:1.62m/s²
def potential_energy(mass, height, gravity):
    return mass * gravity * height

def user(name, email, membership):
    print(f'{name} {email} {membership}')

import math
def calc_triangle(w, h, angle=90):
    area = (1/2) * w * h * math.sin(math.radians(30))
    return area

print(round(math.sin(math.radians(30)),3)) # 무리수인 파이
print(math.sin(math.radians(45)))
print(math.sin(math.radians(60)))
print(math.sin(math.radians(90)))
print(math.sin(math.radians(120)))
print(math.sin(math.radians(135)))
print(math.sin(math.radians(150)))
print(math.sin(math.radians(180)))