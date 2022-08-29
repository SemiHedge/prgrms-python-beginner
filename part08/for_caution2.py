# remove 개선
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
for name in member.copy():
    if name[0] in ['A', 'a']:
        member.remove(name)
print(member)


# append 개선
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
for name in member[:]:
    if name[0] in ['A', 'a']:
        member.append(name)
print(member)