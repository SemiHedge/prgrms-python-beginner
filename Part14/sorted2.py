cars = {
    '삼각형차': 90,
    '표범차': 150,
    '황소차': 200, 
    '왕관차': 120,
    '말차': 180
}

faster_cars = sorted(
    cars.items(),
    key = lambda x: x[1],
    reverse = True
)
print(faster_cars)
print(dict(faster_cars))