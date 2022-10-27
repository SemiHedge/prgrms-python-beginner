# 회원가입 아이디 입력
username = input("가입할 아이디 : ")

# 가입할 아이디는 최대 12자까지만 가능합니다.
if len(username) <= 12:
    print("사용 가능한 아이디입니다.")
else:
    print(f"최대 글자 수(12)를 넘었습니다. {username} - {len(username)}자")