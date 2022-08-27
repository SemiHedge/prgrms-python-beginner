# 이미 살펴본 파라미터 기본값 지정
# 멤버십이 처음에는 Bronze
def user(name, email, membership='Bronze'):
    print(f'가입완료 {name} {email} {membership}')


user('스펜서', 'spencer@grepp.co')
number = 3