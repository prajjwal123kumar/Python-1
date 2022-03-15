#WAP find a largest no. in list
l1=[3,2,9,7,5]
fn=l1[0]
for i in range(1,len(l1)):
    if fn<l1[i]:
        fn=l1[i]
    i=i+1
print(fn)
