# dict_for
basket = {
    'apple': 3,
    'banana': 5,
    'pineapple': 6,
    'lemon': 7
}

for item in basket:
    print(f'{item}은 {basket[item]}개 있습니다.')

for key, value in basket.items():  # [('apple', 3),...]
    print(f'{key}은 {value}개 있습니다.')