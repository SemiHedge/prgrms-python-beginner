# 리스트 컴프리헨션과 map의 비교
# 빌트인 함수
# list comprehension
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
chars = [str(n) for n in nums]
print(chars)


# map
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
chars = list(map(str, nums))
print(chars)


# 기본 연산
# list comprehension -> 단순식, 함수가 있다면 호출식을 적음
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = [n**2 for n in nums]
print(new_nums)


# map -> 무조건 함수로 줘야함
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = list(map(lambda n: n**2, nums))
print(new_nums)


# lambda를 이용한 연산
# list comprehension -> 단순식, 함수가 있다면 호출식을 적음
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = [(lambda n: 2*n+1)(n) for n in nums]
print(new_nums)


# map -> 무조건 함수로 줘야함
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = list(map(lambda n: 2*n+1, nums))
print(new_nums)
