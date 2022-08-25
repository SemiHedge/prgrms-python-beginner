# case1
sport = 'soccer'
if sport == 'soccer' or sport == 'baseball' or sport == 'basketball':
    print("조사항목")
else:
    print("비조사항목")

# case2 - falsy 이용
sport = 'soccer'
check_sports = ['soccer', 'baseball', 'basketball']
if check_sports.count(sport) >= 1:
    print("조사항목")
else:
    print("비조사항목")

# case3 - in 연산자
sport = 'soccer'
check_sports = ['soccer', 'baseball', 'basketball']
if sport in check_sports:
    print("조사항목")
else:
    print("비조사항목")