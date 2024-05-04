number = int(input("Input a decimal integer less than 100:"))


fifties = number // 50


temp = number % 50
tens = temp // 10

temp2 = temp % 10
fives = temp2 // 5

temp3 = temp2 % 5
ones = temp3

p_fifties = (fifties*"L")
p_tens = (tens*"X")
p_fives = (fives*"V")
p_ones = (ones*"I")

print(p_fifties, p_tens, p_fives, p_ones,sep="")


print







