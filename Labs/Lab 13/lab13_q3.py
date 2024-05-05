def sum_double_recursive(n):
    if n <= 0:
        return 0
    else:
        return n + sum_double_recursive(n - 1) + sum_double_recursive(n - 2)
    
print(sum_double_recursive(5))


"""
5 + rec4 + rec3
5 + 4 + 3 + rec3 + rec2 + rec2 + rec1
5 + 4 + 3 + 3 + 2 + 2 + 1 + rec2 + rec1 + rec1 + rec1
5 + 4 + 3 + 3 + 2 + 2 + 1 + 2 + 1 + 1 + 1 + rec 1
5 + 4 + 3 + 3 + 2 + 2 + 1 + 2 + 1 + 1 + 1 + 1
26
"""