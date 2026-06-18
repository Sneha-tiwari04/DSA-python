def tb(n,l):
    if l==0:
        return 1
    tb(n,l-1)
    print(n*l)