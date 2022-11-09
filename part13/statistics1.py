import statistics
nums = [1, 2, 3, 4, 7, 7, 9, 99, 5]

print(sum(nums)/len(nums))
print(statistics.mean(nums))
print(statistics.median(nums))  # 중앙값
print(statistics.mode(nums))  # 최빈값


