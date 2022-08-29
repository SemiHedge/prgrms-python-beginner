# for문에서의 수정(update)
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
for name in member:
    if name[0] in ['A', 'a']:
        name = 0
print(member)
# 기대 : ['Spencer', 0, 0, 'Chen', 'John', 0, 0, 'Darby']
# 실제 : ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']


# 개선 update -> index를 생성 -> for문의 장점이 살리지 못함 -> enumerate
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
index = 0
for name in member:
    if name[0] in ['A', 'a']:
        member[index] = 0
    index += 1
print(member)