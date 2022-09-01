# while vs for
# for문에서의 수정(update)
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
index = 0
for name in member:
    if name[0] in ['A', 'a']:
        member[index] = 0
    index += 1
print(member)


# while문으로 수정
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
index = 0
while index < len(member):
    if member[index][0] in ['A', 'a']:
        member[index] = 0
    index += 1
print(member)