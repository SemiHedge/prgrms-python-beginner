import random
n1 = random.random()  # 0~1 float
n2 = random.randint(0, 255)  # 0~255 int
n3 = random.uniform(0, 255)  # 0~255 float
print(n1, n2, n3)

# seed -> 마인크래프트 맵 seed
random.seed(0)
print(random.random())
print(random.random())
random.seed()
print(random.random())
print(random.random())

# choice
nums = list(range(1, 46))
print(random.choice(nums))
print(random.sample(nums, 6))

# shuffle
print(nums)
random.shuffle(nums)
print(nums)