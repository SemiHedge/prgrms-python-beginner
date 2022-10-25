users = [
    {'name': '머쓱이', 'part': 'AI', 'pay': 50000},
    {'name': '스펜서', 'part': 'BackEnd', 'pay': 15000},
    {'name': '쓰쓱이', 'part': 'FrontEnd', 'pay': 40000},
]


for user in users:
    if user['pay'] >= 30000:
        print(user)