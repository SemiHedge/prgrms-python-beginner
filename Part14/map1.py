# map(적용함수, 시퀀스데이터)
# 각 요소를 적용함수로 넣었을 때의 return값으로 남겨 반환
# 모든 요소에 대해 처리한다는 것이 list comprehension과 유사해보임

def positive_number(number):
    return number > 0

nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = map(positive_number, nums)
print(new_nums)
print(list(new_nums))


# map + lambda
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = list(map(lambda number: number > 0, nums))
print(new_nums)