# Wap to check input IP address correct or not.
x=input("Enter Ip Address : ")
l1=x.split('.')
flag=0
if len(l1)==4:
    for i in range(len(l1)):
        e=l1[i]
        if e.isnumeric():
            e=int(e)
            if e>=0 and e<=255:
                pass
            else:
                print("IP address is incorrect.")
                flag=1
                break
        else:
            print("IP address is incorrect.")
            flag=1
            break
    if flag==0:
        print("IP address is correct.")
else:
    print("IP address is incorrect.")