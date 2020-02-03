
items = []   #empty list
num = [x for x in input().split(',')]  #taking inputs from user with comma separated and storing in num list
for p in num:   # fetching all the elements from the num list one by one 
    x = int(p, 2)  #coverting the string to decimal number
    if not x%5:  #checking either that decimal no divisible by 5 or not
        items.append(p)  #storing the binary no which are divisible by 5 into the empty list
print(','.join(items))   #  printing the elements with comma separated 



