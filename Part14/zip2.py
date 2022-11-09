cars = [
    ('삼각형차', 90), ('표범차', 150), ('황소차', 200), ('왕관차', 120), ('말차', 180)
]

v1, v2 = zip(*cars)
print(v1, v2)

dict_cars = dict(cars)
print(dict_cars.keys(), dict_cars.values())


cars = [
    ('삼각형차', 90, 'KR'), 
    ('표범차', 150, 'JP'), 
    ('황소차', 200, 'EN'), 
    ('왕관차', 120, 'US'), 
    ('말차', 180, 'DE')
]

v1, v2, v3 = zip(*cars)
print(v1)
print(v2)
print(v3)