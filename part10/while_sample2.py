# 제대로 된 입력할 때까지 
name = input("Enter yourname : ")
while not name:
    print("이름을 제대로 입력해주세요")
    name = input("Enter yourname : ")
print(name)


# 대안
name = None
while not name:
    print("이름을 제대로 입력해주세요")
    name = input("Enter yourname : ")
print(name)