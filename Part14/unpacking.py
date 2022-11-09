# * unpacking
nums1 = [1, 3, 5, 7, 9, 11]
nums2 = [1, 3, 5, 7, 9, 11]
print(*nums1)  # print(1, 3, 5, 7, 9, 11)

# 리스트 합친다.
# nums1.extend(nums2)
# new_nums = nums1 + nums2
new_nums = [*nums1, *nums2]
print(new_nums)

dict1 = {'spencer': 100, 'mussg': 20}
dict2 = {'may': 30, 'allen': 15}

# 딕셔너리 합치자
# dict1.update(dict2)
new_dict = {**dict1, **dict2}
print(new_dict)