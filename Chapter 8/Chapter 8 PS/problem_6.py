
#Write a python function which convert inches to cm.


def inch_to_cm(inch):
    return inch * 2.54

n = int(input("Enter the values in Inches : "))

print(f"The corresponding value in cms is  {inch_to_cm(n)}")