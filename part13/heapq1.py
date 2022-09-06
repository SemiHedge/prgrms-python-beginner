import heapq
nums = [1, 2, 3, 4, 5, 6, 7, 7, 7]

print(min(nums), max(nums))
print(heapq.nlargest(2, nums))
print(heapq.nsmallest(4, nums))
print(heapq.nlargest(2, nums)[-1])
print(heapq.nsmallest(4, nums)[-1])