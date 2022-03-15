# Variable Length Argument Function
# Write code for sum
def sum(args):
    sum=0
    if (len(args)!=0):
        for e in args:
            sum=sum+e
    print(sum)
t1=()
sum(t1) # 0
t2=(1,3,5,7)
sum(t2) # 16