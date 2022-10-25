users = [
    {'name': '머쓱이', 'part': 'AI', 'pay': 50000},
    {'name': '스펜서', 'part': 'BackEnd', 'pay': 15000},
    {'name': '쓰쓱이', 'part': 'FrontEnd', 'pay': 40000},
]

# 리스트 for문 + 딕셔너리 for문을 이용하여 '출력예시'처럼 나오도록 코드를 작성하세요
for index, user in enumerate(users, 1):
    print(f'==={index}번 유저 정보===')
    for key, value in user.items():
        print(key, '>', value)
    print()