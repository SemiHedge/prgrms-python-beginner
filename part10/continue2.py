from ast import keyword


member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
# 이름이 특정 문자가 있는 사람은 스킵하자
char = 'n'

for user in member:
    if char in user:
        continue
    print(user)