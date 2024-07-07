# With help of type function we can print any type of variable and know there type 
a = 32
 
t = type(a) #class <int>
print(t)

b = 21.2
x = type(b)
print(x)

# we can also convert any type of variable into any type but condition is variable should be meet there type.

p = "31.2"
b = float(p) # p but the type should be float
z = type(b)
print(z)