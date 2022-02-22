# WAP to convert all even index position to upper case & all odd position to lower case of input string.
x=input("Enter Any String : ")
y=""
i=0
while i<len(x):
    ch=x[i]
    code=ord(ch)
    if i%2==0:
        if code>=97 and code<=122:
            code-=32
    else:
        if code>=65 and code<=90:
            code+=32 
    y+=chr(code)
    i+=1
print(y)