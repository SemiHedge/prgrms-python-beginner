# 리스트 컴프리헨션의 filter처럼 사용
# filter + lambda
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = list(filter(lambda number: number > 0, nums))
print(new_nums)

# [남을 값 for item in list if 조건식]
# listcomprehension + if
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = [n for n in nums if n > 0]
print(new_nums)

# listcomprehension + if 이 유리한 점?
# 남을 값에 추가 연산을 더 해줄 수 있다.
# [남을 값 for item in list if 조건식]
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = [n+5 for n in nums if n > 0]
print(new_nums)