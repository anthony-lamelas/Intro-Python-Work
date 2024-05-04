import random

dict = {x : f'{random.uniform(-100.0,101.0):.3f}' for x in range (0,101)}

print(dict)