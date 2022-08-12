# dict sample
# create
user1 = {
    'name' : '스펜서',
    'college' : '프로그래머스',
    'year' : 20
}
print(user1)

# access > update
user1['name'] = '머쓱이' 
user1['year'] += 1
print(user1)

# add
user1['lang'] = 'Python'
print(user1)

# delete
del user1['college']
print(user1)