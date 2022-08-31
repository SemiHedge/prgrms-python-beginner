basket = {
    'apple': 3,
    'banana': 4,
    'pineapple': 5,
    'orange': 6
}

for item in basket:
    print(item)
    print(f'{item}는 {basket[item]}개 있습니다.')

for key, value in basket.items():  # [('apple', 3), ...]
    print(key, value)
    print(f'{key}는 {value}개 있습니다.')
