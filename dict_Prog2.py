# CRUD in Dictionary

# 1.How to read dictionary element ? 

#   Here we can Read element 2 types.
# 1. Read data with direct key
d1={'a':'ABC',3:'abc3',3.5:'xyz3.5',5:(1,4,5,3)}
x=d1['a']
print(x)
# 2. Read data with get() method.
d1={'a':'ABC',3:'abc3',3.5:'xyz3.5',5:(1,4,5,3)}
y=d1.get(3,"NA") 
print(y)
z=d1.get(40,"NA")
print(z)
# Here, key is not found return default value(any value).

# 2. ADD(Create) & Update

# dict_object[key]=value

# If key is not exists then new key created & value stored at key index.
d1['abc']='PQRS'
print(d1)
# If key exists then value update at key index.
d1['abc']='Prajjwal'
print(d1)

# 3. Delete : Here we can delete element 2 types

# 1. d1.pop(key) : Delete only one key which we will pass

d1.pop(3)
print(d1)

# 2. d1.popitem() : Delete last key

d1.popitem()
print(d1)