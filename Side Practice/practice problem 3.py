import math


velocity = float(input("Enter the initial velocity: "))
angle = float(input("Enter a launch angle between 0 and 90: "))
height = float(input("Enter the height: "))
gravity = float(input("Enter the gravity: "))


max_height = (((velocity ** 2) * (math.sin(angle))**2)/gravity*2) + height

print(max_height)

flight_time = (2*velocity*math.sin(angle))/gravity

print(flight_time)

horizontal_range = ((velocity**2) * math.sin(2*angle))/gravity

print(horizontal_range)

print(math.sin(45))
