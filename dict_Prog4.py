# Loop in dictionary : In dictionary 4 types of loop. And Range loop not support in dictionary.
d1={'a':'ABC',3:24,3.5:90}
# 1st loop
for e in d1:
    print(e)
# 2nd loop
for e in d1.keys():
    print(e)
# 3rd loop
for e in d1.values():
    print(e)
# 4th loop
for e in d1.items():
    print(e)