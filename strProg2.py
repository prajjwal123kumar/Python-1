
x="I am anil singh"
y=x.index('am')
print(y)
print(x.index('i')) # default start 0 index and end last index till.
print(x.index('i',3)) # now start will 3 index
print(x.index('i',8,12)) # this function end here 12 index position
print(x.rindex('a')) # this function search index i to right side
print(x.find('a')) # this function find a then given index position or not get then -1
print(x.rfind('n')) # find right side
print(x.count('a')) # this function tell how many time a came here
