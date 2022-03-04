l1=[1,3,5]
l2=[11,33,55]
print(l1,l2) # [1, 3, 5] [11, 33, 55]
l1[0]=111
l2[1]=222
print(l1,l2) # [111, 3, 5] [11, 222, 55]
l1=l2 # Assignment Operator always store reference
print(l1,l2) # [11, 222, 55] [11, 222, 55]
l1[1]=32
l2[2]=56
print(l1,l2) # [11, 32, 56] [11, 32, 56]