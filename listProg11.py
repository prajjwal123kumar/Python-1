# functions of List
# CRUD Operation : 
# C=For Create
# 1. append()=> Always returntype None.And add element at the end of list.
l1=[1,3,5]
l1.append(7)
print(l1) # [1, 3, 5, 7]

# 2. insert()=> Always returntype None. To add element indexwise.
l1=[1, 3, 5, 7]
l1.insert(1,2)
print(l1) # [1, 2, 3, 5, 7]
l1.insert(2,[1,3,7])
print(l1) # [1, 2, [1, 3, 7], 3, 5, 7]
a=len(l1)
print(a) # 6
l1[2][1]
l1[2].insert(2,5)
print(l1) # [1, 2, [1, 3, 5, 7], 3, 5, 7]
l1[2].insert(1,[11,22,33])
print(l1) # [1, 2, [1, [11, 22, 33], 3, 5, 7], 3, 5, 7]
a=l1[2][3]
print(a) # 5
b=l1[2][1]
print(b) # [11, 22, 33]

# 3. extend()=> Always returntype None.
#               To add element of iterator or collection into list(end of list).

l1=[1,3,5]
l1.extend('abc')
print(l1) # [1, 3, 5, 'a', 'b', 'c']

l1=[1,3,5]
l2=[3,7,8]
l1.extend(l2)
print(l1) # [1, 3, 5, 3, 7, 8]

# R=For Read
# 1. index(self,element,start,end)=>Always returntype is int.It works only int,float,str type of element
l1=[1,2,2.5,4]
a=l1.index(2.5) # return index position
print(a) # 2
# 2. count(self,element.start,end)=>Always returntype is int.
l1=[1,2,2,4]
x=l1.count(2) # return how many times has come element
print(x) # 2

# U=For Update
# By default use this
l1=[1,3,5]
l1[1]=7
print(l1) # [1, 7, 5]

# D=>For Delete
# 1. remove(self,element)=>
l1=[1,3,5,7]
l1.remove(5)
print(l1) # [1, 3, 7]

# 2. pop(self,index)=>
l1=[1,3,5,7]
l1.pop() # Delete only last element one by one. when by default no index position pass 
print(l1) # [1, 3, 5]
 
l1=[1,3,5,7]
l1.pop(1) # Delete only which index position we will pass
print(l1) # [1, 5, 7]
