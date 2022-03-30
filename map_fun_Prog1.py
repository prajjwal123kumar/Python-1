# map=(callable_function,*Iterators)
# Always return type is Iterator.
l1=[1,3,5,7]
l2=[3,2,9,11]
l3=[11,22,33,44]
def some_work(no1,no2,no3):
    no=((no1+no2+no3)*2)+4
    return no

It4=map(some_work,l1,l2,l3)
l4=list(It4)
print(l4)