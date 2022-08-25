# if문
number = 20

if number == 20:
    print("1. Correct!")

if number > 20:
    print("2. Correct!")


# user info
user = input("Enter Yourname : ")
admin = "mussg"

if user.lower() == admin:
    print("Welcome!")
    print(f"Hello {user}")

print("End")


# number info
answer = int(input("Enter Number : "))
goal = 30

if answer == goal:
    print("Correct!")