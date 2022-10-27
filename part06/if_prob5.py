# 회원가입 아이디 입력
member = ['spencer', 'mark1234', 'program', 'mussg3243']
username = input("가입할 아이디 : ")

# 조건문 작성
if ' ' in username:
    print('아이디에 공백을 포함할 수 없습니다.')
elif username in member:
    print('이미 사용하는 아이디입니다.')
elif len(username) < 6:
    print("최소 글자 수는 6입니다.")
elif len(username) > 12:
    print("최대 글자 수는 12입니다.")
else:
    print(f"사용 가능한 아이디입니다.")