# for문 도중 member의 remove > 넘어가는 데이터가 생김
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
for name in member:
    if name[0] in ['A', 'a']:
        member.remove(name)
print(member)
# 기대 : ['Spencer', 'Chen', 'John', 'Darby']
# 실제 : ['Spencer', 'Allen', 'Chen', 'John', 'Andy', 'Darby']
# 디버그 -> watch로 member, name 찍어두기
# python tutor로 실행해보기


# for문 도중 member의 append > 끝나지 않음, 추첨권 우선권
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
for name in member:
    if name[0] in ['A', 'a']:
        member.append(name)
print(member)

