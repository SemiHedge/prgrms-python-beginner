user = ['스펜서', '머쓱이']

try:
    print(user[2])
except IndexError:
    print("리스트 인덱스 범위 밖입니다.")
except:
    print("오류 제어")