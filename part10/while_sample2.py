# 제대로 된 입력할 때까지 
name = input("Enter yourname : ")
while not name:
    name = input("Enter yourname : ")
print(name)


name = None
while not name:
    name = input("Enter yourname : ")
print(name)