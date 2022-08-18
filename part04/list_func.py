# list func
# sort()
nums = [33, 22, 11, 77, 55, 66, 99, 88]
nums.sort()
print(nums)

# sort(reverse=True)
nums = [33, 22, 11, 77, 55, 66, 99, 88]
nums.sort(reverse=True)
print(nums)

# .reverse()
nums = [33, 22, 11, 77, 55, 66, 99, 88]
nums.reverse()
print(nums)

# .remove(v)
nums = [33, 22, 11, 77, 55, 66, 99, 88]
nums.remove(11)
print(nums)

nums = [33, 22, 11, 77, 55, 66, 11, 99, 88]
nums.remove(11)
print(nums)

# .index(v)
nums = [33, 22, 11, 77, 55, 66, 99, 88]
print(nums.index(11))

# .extend(v)
nums1 = [33, 22, 11, 77]
nums2 = [55, 66, 99, 88]
nums1.extend(nums2)
print(nums1)

nums3 = nums1 + nums2
print(nums3)

# .count(v)
nums = [33, 22, 11, 77, 55, 66, 11, 99, 88]
print(nums.count(77))

# .pop(i) .pop()
nums = [33, 22, 11, 77, 55, 66, 11, 99, 88]
num = nums.pop()  # del nums[1] -> None
print(num)

# len()
nums = [33, 22, 11, 77, 55, 66, 11, 99, 88]
print(len(nums))

# sorted(v), sorted(v, reverse=True)
nums = [33, 22, 11, 77, 55, 66, 11, 99, 88]
print(sorted(nums)) 
print(nums) 
print(sorted(nums, reverse=True)) 
print(nums) 