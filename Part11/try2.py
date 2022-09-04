# 처리할 데이터에 예상치 못한 값, 상황이 발생할 때
# y = 2/x + 1
nums = [0, 3, 9, 12, 'a', 'x', 15]
results = []
for x in nums:
    try:
        print(f'2/{x} + 1 = {2/x + 1}')
    except (ZeroDivisionError, TypeError) as e:
        # print(e)    
        print(f'{x} -> 0 또는 숫자가 아닌 데이터는 처리 불가')    
    except Exception as e:  # 1
        print(e)