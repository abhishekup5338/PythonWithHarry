
#Write a program using function to convert celsius to fahrenheit.


def f_to_c(f):
      return 5*(f-32)/9
      
f = int (input("Enter the temprature in F: "))
c = f_to_c(f)
# print(f_to_c(f))

print(f"{round(c,2)}°C")
