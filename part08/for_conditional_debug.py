# Conditional Breakpoint
for x in range(100):
    print(x)

# Conditional Breakpoint
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
for name in member.copy():
    if name[0] in ['A', 'a']:
        member.remove(name)
        # print(f'현재 member : {member}')
print(member)