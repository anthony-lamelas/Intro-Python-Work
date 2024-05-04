import math

def numbers(num1,num2,num3,num4,num5):
    sum = num1+num2+num3+num4+num5
    mean = sum/5.0
    product = num1*num2*num3*num4*num5
    root = math.sqrt(product)
    return(sum,mean,product,root)


print(numbers(3,4,5,6,7))