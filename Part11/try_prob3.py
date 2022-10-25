users = [
    {'name': '머쓱이', 'birth_date': '1999-11-13'},
    {'name': '스펜서', 'birth_date': '2000-01-03'},
    {'name': '쓱쓱이', 'birth_date': '2001-03-22'},
    {'name': '머펜서', 'birth_date': '2004-07-28'},
    {'name': '펜쓱이', 'birth_date': '20051013'},
]


# 함수를 만듭니다.
def get_birth_year(date):
    try:
        date = date.split('-')
        return 2200 - int(date[0])  # 2200년 기준 만 나이 계산
    except:
        print("연도를 추출할 수 없습니다.")
        return None


# 함수 실행
for user in users:
    age = get_birth_year(user['birth_date'])
    user['age'] = age
    print(user)
