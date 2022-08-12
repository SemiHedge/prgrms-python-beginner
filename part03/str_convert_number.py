# str convert int
year = "2020"
# year += 2  # TypeError
print(year)

year = int("2020")
year += 2
print(year)

# error
greet = int("hello")  # ValueError
print(greet)