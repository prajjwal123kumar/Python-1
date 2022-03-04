l2=['Hello','Hi',7.5,3729]
a=l2[0]
print(a)
b=l2[1]
print(b)
c=l2[0][2]
print(c)

# d=l2[1][0]='A'
# print(d) #  Here Error will come. ( Because string is immutable we can not modify string but We can do indexing. )


l2[0]=25
print(l2) #[25, 'Hi', 7.5, 3729] ( Because list is mutable we can modify list and We can do indexing. )

