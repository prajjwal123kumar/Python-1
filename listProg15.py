# WAP to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
l1=['aba' , 'abc' , 'aaaab', '1232', '3333']
c=0
for e in l1:
    if(len(e)>=2 and (e[0]==e[len(e)-1])):
        c+=1
print(c)
