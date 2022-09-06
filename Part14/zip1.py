users = ['Spencer', 'Mussg', 'John', 'Allen']
ages = [100, 20, 40, 70]

new_list = list(zip(users, ages))
print(new_list)

new_dict = {k: v for k, v in zip(users, ages)}
print(new_dict)


xs = [3, 5, 7, 9]
ys = [2, 5, 8, 4]
for x, y in zip(xs, ys):
    print(f'{x} * {y} = {x*y}')
