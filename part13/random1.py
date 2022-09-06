import random
n1 = random.random()  # 0~1
n2 = random.randint(0, 255)  # 0~255 int
n3 = random.uniform(0, 255)  # 0~255 float

# 마인크래프트 랜덤 시드
# 컴퓨터는 기본적으로 난수를 만들 수 없다. -> 난수 생성 알고리즘을 통한 것
# x -> y
# 보통은 현재 시간
# seed
random.seed(0)
print(random.random())
print(random.random())

# choice
nums = list(range(1,46))
print(random.choice(nums))
print(random.sample(nums, 6))

# shuffle
print(nums)
random.shuffle(nums)
print(nums)