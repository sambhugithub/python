
from operator import itemgetter, attrgetter#import libraries for to maintain the order of sorting
def sort(*args): #function definition with taking argument as list which contains tuples 
    return sorted(l, key=itemgetter(0,1,2)) #returning sorted list..0,1,2 is nothing but we are providing the priority of index in the tuple

l = [] #empty list 
while True:#loop
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))#taking input from user as tuples and stroing in a list
p=sort(l)#function call
print(p)#print the sorted list which contains the tuples as elements