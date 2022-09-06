import statistics
nums = [1, 2, 3, 4, 5, 6, 7, 7, 7]
print(sum(nums)/len(nums))
print(statistics.mean(nums))  # 평균값
print(statistics.median(nums))  # 중간값
print(statistics.mode(nums))  # 최빈값
