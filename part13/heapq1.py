import heapq
nums = [1, 2, 3, 4, 5, 8, 7, 6]

print(max(nums), min(nums))
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
print(heapq.nlargest(3, nums)[-1])
print(heapq.nsmallest(3, nums)[-1])