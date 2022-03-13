l1=[1,3,5]
l2=l1
l1[0]=11
l2[1]=22
print(id(l1),id(l2)) # [11, 22, 5] [11, 22, 5]
# 19852808 19852808

# Use copy()=> Address will change l1 and l2 
l2=l1.copy() # Create a new object
l1[0]=11
l2[1]=22
print(id(l1),id(l2)) # [11, 22, 5] [11, 22, 5]
# 19852808 20857768