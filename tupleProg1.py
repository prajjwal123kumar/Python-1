# Tuple=> Tuple is a immutable collesction of hetrogeneous datatype.
# syntax:
# Variable Name=(Comma seperated elements)

t1=(1,3.5,'abc',97)
print(type(t1)) # <class 'tuple'>

a=t1[0]
print(a) # 1

# t1[1]=75
# print(t1) # TypeError: 'tuple' object does not support item assignment

# Slicing in Tuple
t2=t1[0:2]
print(t2)