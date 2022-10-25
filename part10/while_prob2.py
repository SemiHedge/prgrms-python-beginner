users = [
    {'name': '머쓱이', 'part': 'AI', 'pay': 2000},
    {'name': '스펜서', 'part': 'BackEnd', 'pay': 10000},
    {'name': '쓰쓱이', 'part': 'FrontEnd', 'pay': 3000},
    {'name': '숲헨서', 'part': 'Embedded', 'pay': 5000},
    {'name': '멍쓱이', 'part': 'IOS', 'pay': 7000},
    {'name': '수헨서', 'part': 'Android', 'pay': 1500},
]

# 페이가 5000 미만인 분들은 페이를 2500씩 올려드리겠습니다 
index = 0
while index < len(users):
    if users[index]['pay'] < 5000:
        users[index]['pay'] += 2500
    index += 1

# 출력 결과
print(users)