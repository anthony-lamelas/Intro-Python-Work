fuel = 100 # Initial rocket fuel
launches = 1 # Number of rocket launches
while fuel > 0:
    print(launches,"launches:", end = "")
    for consumption in range(fuel, 0, -fuel//5):
        print(consumption, "->", end = "")
    if fuel > 10:
        print("Blastoff!")
    else:
        print("Rocket grounded.")
    fuel //= 5 # Simulate fuel consumption using integer division
    launches += 1
