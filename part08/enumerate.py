# enumerate
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
print(list(enumerate(rainbow)))

for i,v in enumerate(rainbow):
    print(f'{i}번째 색은 {v}')
