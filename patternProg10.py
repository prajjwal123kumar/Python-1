n=int(input("Enter No. of Lines : "))
for i in range(1,n+1):
    for k in range(2*(i-1)):
        print(" ",end="")
    for j in range(n-(i-1)):
        print(" *",end="")
    print()
    

n=int(input("Enter No. of Lines : "))
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    for m in range(n-(i-1)):
        print("*",end=" ")
    print()