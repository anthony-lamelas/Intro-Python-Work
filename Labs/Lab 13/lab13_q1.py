def mystery(n):
    if n == 0:
        return 1
    else:
        return n * mystery(n - 1)
def main():
    print(mystery(4))
    
main()


"""
4 x 3 x 2 x 1 x 1
24

"""