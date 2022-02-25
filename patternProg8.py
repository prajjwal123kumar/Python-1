# Inverted Full Pyramid Pattern *
n=int(input("Enter No. of Lines : "))
for i in range(1,n+1):
    for k in range(i-1):
        print(" ",end="")
    for j in range(n-(i-1)):
        print("*",end=" ")
    print()
    
