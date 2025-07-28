n=int(input("enter number of rows: "))
for i in range (1, n+1):
    for s in range (n-i):
        print(" ",end="")
    for a in range (i):
        print("*",end="")
    print()