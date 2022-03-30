# Use of Delegation Function
# Example 1

# BLL code start here
def any_operation_on_two_list(l1,l2,any_operation): 
    # here any_operation is a function and address is 1000
    l3=[]
    for i in range(len(l1)):
        s=any_operation(l1[i],l2[i])
        l3.append(s)
    print(l3)
# BLL code ends here

# PL code start here
l1=[1,3,5,7]
l2=[11,22,33,44]
print(l1,l2)
def sum(n1,n2): # sum=any_operation, address of sum is same 1000.
    return(n1+n2)
any_operation_on_two_list(l1,l2,sum)
# PL code ends here