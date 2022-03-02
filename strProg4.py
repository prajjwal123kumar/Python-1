# String Formatting.
# .format()=> always return type str.
fn=input("Enter first name : ")
ln=input("Enter last name : ")
age=input("Enter age : ")

# fullstring="My name is "+fn+" "+ln+" and my age is "+age+" years."
# print(fullstring)

# fullstring="My name is {fn} {ln} and my age is {age} years.".format(fn=fn,ln=ln,age=age)
# print(fullstring)

fullstring="My name is {0} {1} and my age is {2} years.{0}".format(fn,ln,age)
print(fullstring)