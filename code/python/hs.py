def hs(n):
    if (n < 1):
        n = None
    else:
        length = 1
        while (n != 1):
            if (n % 2 == 0):
                print(n)
                n = n//2
                length = length + 1
            else:
                print(n)
                n = 3*n + 1
                length = length + 1
        print(n)
        print (length)
    
