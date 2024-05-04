import random

flavor = str(input("Enter the cake flavor: "))
ingredient1 = str(input("Enter the first ingredient: "))
ingredient2 = str(input("Enter the second ingredient: "))
ingredient3 = str(input("Enter the third ingredient: "))

name1 = flavor[0:3] + ingredient1[-3:]
name2 = flavor[0:3] + ingredient2[-3:]
name3 = flavor[0:3] + ingredient3[-3:]

print()

print("Generated Cake Names: ")

random = random.randint(0,100)

print("\t", name1, random, sep="")

print("\t", name2, random,sep="")

print("\t", name3, random,sep="")