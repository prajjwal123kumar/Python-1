# center()- always return str
x="hello"
print(x.center(50,"*")) # **********************hello***********************
print(x.ljust(20,"*")) # hello***************
print(x.rjust(20,"*")) # ***************hello



# strip()- always return str. Strip remove spaces both side(left & right)
p="  welcome  "
q=p.strip()
print(q)
print(p.lstrip())
print(p.rstrip())

# join(self,iterable)- always return str. to add data middle in string
x='abcd'
y='Hi'
z=y.join(x)
print(z)
# To add after d like this method 
print(z+"Hi")