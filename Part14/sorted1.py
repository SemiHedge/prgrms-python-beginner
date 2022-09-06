cars = [
    ('삼각형차', 90), ('표범차', 150), ('황소차', 200), ('왕관차', 120), ('말차', 180)
]

# 그냥 정렬
print(sorted(cars))
print(sorted(cars, reverse=True))

# 그냥 속도만 있다면 쉽게 정렬할텐데..
# 속도 순으로 정렬
faster_cars = sorted(
    cars,
    key=lambda car: car[1],
    reverse=True
)

print(faster_cars)

cars = {
    '삼각형차': 90,
    '표범차': 150,
    '황소차': 200, 
    '왕관차': 120,
    '말차': 180
}


faster_cars = sorted(
    cars.items(),
    key=lambda car: car[1],
    reverse=True
)

print(faster_cars)
print(dict(faster_cars))
