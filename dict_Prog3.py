# Method in Dictionary
# 1. fromkeys() : Takes 2 parameters.
# fromkeys(sequence/key , value)

# sequence of keys
x='abcd'
d1=dict.fromkeys(x)
print(d1)
# Keys with value
x=('abcd','xyz')
y=0
d1=dict.fromkeys(x,y)
print(d1)
# mutable object list
x={'a','b','c'}
y=[1]
d1=dict.fromkeys(x,y)
print(d1)
y.append(2)
print(d1)

# 2. clear(): clear all elements of  dictionary

d1={'a': [1, 2], 'b': [1, 2], 'c': [1, 2]}
d1.clear()
print(d1)