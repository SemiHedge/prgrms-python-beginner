# fliter(기준함수, 시퀀스데이터)
# for로 양수만 추출
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = []
for n in nums:
    if n > 0:
        new_nums.append(n)
print(new_nums)

# 함수로 정의
def positive_number_list(nums):
    new_nums = []
    for n in nums:
        if n > 0:
            new_nums.append(n)
    return new_nums

nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
print(positive_number_list(nums))
# 과연 이 함수 얼마나 쓸까?
# 함수의 핵심은 0보다 크다를 구분하는 것


# 기준함수로 넣었을 때 True가 나오는 요소만 남긴다.
def positive_number(number):
    return number > 0

nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = filter(positive_number, nums)
print(new_nums)
print(list(new_nums))


# filter + lambda
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = list(filter(lambda number: number > 0, nums))
print(new_nums)