# WAP to convert input string into lowercase
x=input("Enter any string : ")
i=0
y=""
while(i<len(x)):
    ch=x[i]
    code=ord(ch)
    # print(i,"=>",x[i],"=>",ord(x[i]))
    if code>=65 and code<=90:
        code+=32
    z=chr(code)
    y+=z
    i+=1
print(y)
    
    