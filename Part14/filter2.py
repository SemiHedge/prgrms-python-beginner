# lambda + filter
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = filter(lambda x: x > 0, nums)  # 기준함수
print(list(new_nums))

# list comprehension + 3항 연산자 if else
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = [n-5 for n in nums if n > 0]
print(new_nums)

new_nums = [n if n > 0 else False for n in nums]
print(new_nums)

num = 3 if 1 < 0 else -1
print(num)