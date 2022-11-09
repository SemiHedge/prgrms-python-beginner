# for문 도중 member의 remove > 넘어가는 데이터가 생김
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
for user in member:
    if user[0] in ['A', 'a']:
        member.remove(user)
print(member)
# 기대 : ['Spencer', 'Chen', 'John', 'Darby']
# 실제 : ['Spencer', 'Allen', 'Chen', 'John', 'Andy', 'Darby']


# for문 도중 member의 append > 끝나지않음
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
for user in member:
    if user[0] in ['A', 'a']:
        member.append(user)
print(member)
# 기대 : ['Spencer', 'Adela', 'Adela', 'Allen', 'Allen','Chen', 'John', 'Albert', 'Albert', 'Andy', 'Andy', 'Darby']
# 실제 : 끝나지않음