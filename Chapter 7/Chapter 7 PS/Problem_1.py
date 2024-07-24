#Write a program to find multiplication table of any number
n = int(input("Enter a number : "))

for i in range(1,11):
    print(f"{n} X {i}= {n * i}")