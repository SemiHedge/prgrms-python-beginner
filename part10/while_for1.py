# while vs for
# for
users = ['Allen', 'Chen', 'John', 'May']
for user in users:
    # print(f'{user}가 입장을 했습니다.')
    user = 0
print(users)


# while
users = ['Allen', 'Chen', 'John', 'May']
index = 0
while index < len(users):
    users[index] = 0
    # print(f'{users[index]}가 퇴장하셨습니다.')
    index += 1
print(users)
