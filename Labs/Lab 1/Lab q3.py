PI = 3.1416

scoops = int(input("Enter the number of ice cream scoops you want:"))
radius = float(input("Enter the radius of the ice cream cone:"))
height= float(input("Enter the height of the ice cream cone:"))

scoops_vol = scoops * (4/3) * PI * (radius**3)
cone_vol = PI * (radius**2) * (height/3)

volume = scoops_vol + cone_vol

print("Your", scoops, "scoop ice cream cone has a total volume of", volume)



