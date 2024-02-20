import math
 #general formular : a1 = ar**(n-1)

a2 = int(input("The first term :"))
r = int(input("The common ratio :"))
n = int(input("The number of the term :"))

a1 = a2*r**(n-1)
print("the ",n,"th term of the GP is :",a1)