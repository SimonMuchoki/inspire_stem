friends = ("Farid","Ian","Hellen","Jay","Ephraim")
for friend in friends:
          print(friend)

enemies = friends[:]   #to copy one list to another       

#enemies = enemies.append("Jay")

for  enemy in enemies :
        print(enemies)

fruits = ["mango", "apple", "pineapple","guava"]   
#slice the list

#print(fruits[0:3])     #slice the list

del fruits[0]
print(fruits)


squares = [] #initializes an empty list
for x in range(0,11):
        squares.append(x**2)

print(squares)       

