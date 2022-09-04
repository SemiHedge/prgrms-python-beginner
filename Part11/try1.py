try:
    1/0
except:
    pass

try:
    1 + "가"
    # int('가'
except ValueError as ve:
    print(f'>>> {ve}')
except Exception as e:
    print(f'>>> {e}')

try:
    num = 3
    print(num)
except Exception as e:
    print(f'>>> {e}')
finally:
    print('마무리 수행')


try:
   # 수행, 시도할 코드
   pass
except ValueError:
   # ValueError 예외 처리
   pass
except (ZeroDivisionError, TypeError):
   # ZeroDivisionError, TypeError 예외 처리(다중)
   pass
except:
   # 그 외 모든 예외 처리
   pass