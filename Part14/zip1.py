users = ['Spencer', 'Mussg', 'John', 'Allen']
ages = [100, 20, 40, 70]

new_list = list(zip(users, ages))
print(new_list)
print(dict(new_list))

# dict comprehension
new_dict = {k: v-1 for k, v in zip(users, ages)}
print(new_dict)


#
xs = [3, 5, 7, 9]
ys = [2, 5, 8, 4]
zs = [0, 1, 3, 6]
for x, y, z in zip(xs, ys, zs):
    print(f'{x} * {y} * {z} = {x*y*z}')