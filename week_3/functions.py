# funtions are a block of code running as a unit
# we first intialize the function
# then call the function
#there are two types pf functions :user defined function and built in function


#this is how to define a function
def print_name():
          print("my mame is Simon")

#calling the function
print_name()             #you can call it as many times as possible

def print_details(name, age, id ,gender):
        print("i am {0},{1} years old, my id number is {2} and my gender is {3}".format(name,age,id,gender))

print_details("Simon","17","12345","male")

def sum_nums(x,y):
        return x+y

z = sum_nums(10,20)
print(z)

def pro_nums(X,Y):
        return X*Y
print(pro_nums(5,6))


#how to use for loop in the function

def print_odds(first_number,last_number):
        for i in range(first_number,last_number):
                if i % 2 :
                        print(i)

print_odds(0,99)

                
