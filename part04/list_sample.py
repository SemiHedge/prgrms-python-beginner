# list
# create
list_num = [0,1,2,3,4,5,6,7]
list_char = ['a','b','c','d','e']
list_str = ['Allen','Chen','John','Mark']
print(list_num, list_char, list_str, sep='\n', end='\n\n')

# access, update
list_num[0] = 777
list_char[3] = 'p'
list_str[2] = "Spencer"
print(list_num, list_char, list_str, sep='\n', end='\n\n')

# delete
del list_num[0]
del list_char[-1]
del list_str[-2]
print(list_num, list_char, list_str, sep='\n', end='\n\n')