try:
    result = '0' / 0
except ZeroDivisionError:
    print("나누기 연산은 0으로 수행할 수 없습니다.")
except TypeError:
    print("str형 데이터와 int형 데이터는 서로 나눌 수 없습니다.")
except:
    print("오류 제어")