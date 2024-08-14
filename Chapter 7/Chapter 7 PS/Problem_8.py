#Write a program to get table of any number in reverse feed.

n = int(input("Enter a number : "))

for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")