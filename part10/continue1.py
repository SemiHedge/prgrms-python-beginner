# orange는 빼고 먹자
basket = ['apple', 'banana', 'orange', 'melon']

# for 변수명 in 리스트:
for item in basket:
    if item == 'orange':
        continue
    print(f'{item}을 먹었습니다.')