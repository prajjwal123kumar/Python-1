# Hellow Inverted Half Pyramid to for loop
n=int(input("Enter no.of lines : "))
for i in range(1,n+1):
    if i==1:
        for j in range(n):
            print("*",end=" ")
    else:
        print("*",end=" ")
        for k in range(n-i-1):
            print(" ",end=" ")
        if(i!=n):
            print("*",end=" ")
    print()

