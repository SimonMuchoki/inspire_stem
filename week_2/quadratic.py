import math

a = float(input("enter first co_efficient :"))
b = float(input("enter second co_efficient :"))
c = float(input("enter constant :"))

d = (b**2)-(4*a*c)

x_1 = (-b-math.sqrt(d)/2*a)
x_2 = (-b+math.sqrt(d)/2*a)



print(x_1)
print(x_2)


