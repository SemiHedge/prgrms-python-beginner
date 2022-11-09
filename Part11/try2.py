# 처리할 데이터에 예상치 못한 값, 상황이 발생할 때
# y = 2/x + 1
nums = [0, 3, 9, 12, 'a', 'x', 15]

for x in nums:
    try:
        print(f'2/{x} + 1 = {2/x + 1}')
    except (ZeroDivisionError, TypeError) as e:
        print(f'>>> Error : {e}')
    except Exception as e:
        print(e)
