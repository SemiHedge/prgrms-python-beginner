# enumerate()
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
# 1번째 색깔은 red
# 2번째 색깔은 orange

index = 0
for color in rainbow:
    # print(f'{index+1}번째 색깔은 {color}')
    index += 1

# print(list(enumerate(rainbow)))
# enumerate() + 여러개 변수 할당
for index, color in enumerate(rainbow):  # index, color = (0, 'red')
    print(f'{index}번째 색깔은 {color}')