# 리스트 컴프리헨션과 map의 비교
# 빌트인 함수 - list comprehension
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
chars = [str(n) for n in nums]
print(chars)

# 빌트인 함수 - map
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
chars = list(map(str, nums))
print(chars)


# 기본연산 - list comprehension
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = [n**2 for n in nums]
print(new_nums)

# 기본연산 - map -> 무조건 함수
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = list(map(lambda x: x**2, nums))
print(new_nums)


# lambda를 이용한 연산 + list comprehension
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = [(lambda x:2*x+1)(n) for n in nums]
new_nums = [2*n+1 for n in nums]
print(new_nums)

# lambda를 이용한 연산 + map
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = list(map(lambda x:2*x+1, nums))
print(new_nums)
