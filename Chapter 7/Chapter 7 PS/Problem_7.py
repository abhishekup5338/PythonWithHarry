#Write a program to print following star pattern




n = int(input("Enter a number : "))

for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*n-1), end="")
    print("")