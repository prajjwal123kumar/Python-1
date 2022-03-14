# WAP to print each element of list.
l=[1,3,5,7]
i=0
while(i<len(l)):
    e=l[i]
    print(e)
    # print(l1[i])
    i=i+1
# OR Second Type with for loop
l1=[1,2,3,4,5]
for i in range(len(l1)):
    e=l1[i]
    print(e)
# Element & Collection on for loop : 
l1=[1,3.5,27,'Hello']
for e in l1:
    print(e)
for e in 'Hello':
    print(e)
