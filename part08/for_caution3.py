# for문에서의 수정(update)
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
for user in member:
    if user[0] in ['A', 'a']:
        user = 0
print(member)
# 기대 : ['Spencer', 0, 0, 'Chen', 'John', 0, 0, 'Darby']
# 실제 : ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']


# for문에서의 수정(update) 개선 -> enumerate
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
index = 0
for user in member:
    if user[0] in ['A', 'a']:
        member[index] = 0
    index += 1
print(member)  # ['Spencer', 0, 0, 'Chen', 'John', 0, 0, 'Darby']