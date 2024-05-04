p1 = [2**x for x in range (1, 8)]
print(p1)

p2 = [x for x in range (0,9)  if x%2 == 0 ]
print(p2)

p3 = {x : x**2 for x in range (0,16, 4)}
print(p3)

p4 = {x : [x*1, x*2, x*3, x*4] for x in range (4,9) }
print(p4)