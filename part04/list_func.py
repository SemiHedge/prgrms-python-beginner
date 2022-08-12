# list func
# .sort()
nums = [33,22,11,77,55,66,99,88]
nums.sort(reverse=True)
print(nums)

# .sort(reverse=True)
nums = [33,22,11,77,55,66,99,88]
nums.sort(reverse=True)
print(nums)

# .reverse()
nums = [33,22,11,77,55,66,99,88]
nums.reverse()
print(nums)

# .remove(v)
nums = [33,22,11,77,55,66,99,88]
nums.remove(77)
print(nums)

# .index(v)
nums = [33,22,11,77,55,66,99,88]
print(nums.index(77))

# .append(v)
nums = [33,22,11,77,55,66,99,88]
nums.append(44)
print(nums)

nums = [33,22,11,77,55,66,99,88]
nums += [44]
print(nums)

# .insert(i,v)
nums = [33,22,11,77,55,66,99,88]
nums.insert(3,44)
print(nums)

# .extend(v)
nums1 = [33,22,11,77]
nums2 = [55,66,99,88]
nums1.extend(nums2)
print(nums1)

nums1 = [33,22,11,77]
nums2 = [55,66,99,88]
nums1 += nums2
print(nums1)

# count.(i,v)
nums = [33,22,11,77,55,66,99,88]
print(nums.count(11))

# .pop()
nums = [33,22,11,77,55,66,99,88]
print(nums.pop())
print(nums)
print(nums.pop())
print(nums)

# len(list)
nums = [33,22,11,77,55,66,99,88]
print(len(nums))

# sorted(list)
nums = [33,22,11,77,55,66,99,88]
print(sorted(nums))

# sorted(list, reverse=True)
nums = [33,22,11,77,55,66,99,88]
print(sorted(nums, reverse=True))

