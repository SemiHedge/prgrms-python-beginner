# break 반복문을 정지 continue 다음차례로 스킵
basket = ['apple', 'banana', 'orange', 'melon']

for item in basket:
    if item == 'orange':
        continue  # 현재 반복 차례 Skip
    print(f'{item}을 먹었습니다.')
