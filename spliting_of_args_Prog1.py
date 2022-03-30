#BLL
def sum(*args):
    s=0
    if len(args)!=0:
        for e in args:
            s+=e
    return s
#PL
l1=[(1,2),(1,2,3),(1,7,5),(1,3,2,7,9)]
l2=[]
for e in l1:
    s=sum(*e) # Spliting of args ( Like (1,2),(1,2,3) )
    l2.append(s)
print(l2) # [3, 6, 13, 22]