#Write a program to find whether the number is prime or not.
Number = int(input("Enter a number: "))

for i in range(2, Number):
    if(Number%i) == 0:
        print("The number is not prime")
        break
else:
    print("The number is prime")
