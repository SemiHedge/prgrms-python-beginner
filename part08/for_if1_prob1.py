member = ['스펜서', '도둑인가', '도로묵둑', '도둑', '도동독', '머쓱이']

for person in member:
    if '도둑' in person:
        print(f"{person}님은 추가 검문 대상입니다.")
    else:
        print(f"{person}님은 통과 대상입니다.")