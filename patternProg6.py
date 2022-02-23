n=int(input("Enter No. of Lines : "))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    for k in range((n-i)*2):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()

# For print spaces

n=int(input("Enter No. of Lines : "))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    for k in range((n-i)*2):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()