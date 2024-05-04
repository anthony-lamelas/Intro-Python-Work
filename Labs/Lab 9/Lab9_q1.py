"""
[12, 2, 8]

[A, B, D, A, B, D]


['first', 'middle', 'second']
['second']

[1, 4, 9]

0, 2, 4, 0, 3, 6, 0, 4, 8

"""





result_lst = []
for i in range(2, 5):
    for j in range(3):
        result_lst.append(i * j)
print(result_lst)
