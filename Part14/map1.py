# map(적용함수, 시퀀스데이터)
# 각 요소를 적용함수로 넣었을 때의 return값으로 남겨 반환
# 모든 요소에 대해 처리한다는 것이 list comprehension과 유사해보임
chars = ['1', '2', '3', '4']
nums = map(int, chars)
print(list(nums), chars)


def positive_number(number):
    return number > 0


nums = [-3, 3, 5, -5, 1, 0, 1, 3, 8, -8]
new_nums = list(map(positive_number, nums))
print(new_nums)


# map + lambda
nums = [-3, 3, 5, -5, 1, 0, 1, 3, 8, -8]
new_nums = list(map(lambda x: x > 0, nums))
print(new_nums)
