#1A: B C
#1B: A D

# One reason to choose commas are that they are more convenient and keep 
#things more concise. They do not require additional formatting.

#2A: 13
#2B:
# 3
# 13
#2C: 17
#2D: 18
#2E: 0


import random

rand_slope = random.randint(-5,5)
rand_y_intercept = random.randint(0,10)

print("Welcome to Drawing Parallels! Test whether your line is parallel to the line f(x)=",rand_slope,"x+",rand_y_intercept,sep="")

slope = int(input("Enter a slope:"))
y_intercept = int(input("Enter a y-intercept:"))


if rand_slope == slope:
    if y_intercept != rand_y_intercept:
            print("Your line f(x)=",slope,"x+",y_intercept, " is PARALLEL to the line f(x)=",rand_slope,"x+",rand_y_intercept,sep="")


if rand_slope != slope:
    print("Your line f(x)=",slope,"x+",y_intercept, " is NOT PARALLEL to the line f(x)=",rand_slope,"x+",rand_y_intercept,sep="")
    
if rand_slope == slope:
    if y_intercept == rand_y_intercept:
            print("Your line f(x)=",slope,"x+",y_intercept, " is NOT PARALLEL to the line f(x)=",rand_slope,"x+",rand_y_intercept,sep="")

        
