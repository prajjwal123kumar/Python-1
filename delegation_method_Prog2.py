# Use of Delegation Function
# Example 2 : WAP to perform any operation on every element of Iterator or list and return a new list.

# BLL code start here
def do_any_operation_on_list(l1,any_operation):
    # here any_operation is a function and address is 2000
    l2=[]
    for i in range(len(l1)):
        s=any_operation(l1[i])
        l2.append(s)
    print(l2)
# BLL code ends here

# PL code start here
l1=[1,3,5,7]
print(l1)
def square(no): # square=any_operation, address of square is same 2000.
    return (no*no)
do_any_operation_on_list(l1,square)