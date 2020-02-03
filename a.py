def dev_by5(*args):#function definition with a list argument
    out=[]         #empty list
    for i in args: # fetching all the elements from the args tupple one by one
        x = int(i, 2) #converting the binary no to decimal no
        if x % 5 ==0:  #checking whether the converted decimal no is divisible by 5 or not
            out.append(i) #storing to the empty list
    return out #function is returning the list 

p=dev_by5([x for x in input().split(',')])   #function call with taking the user input with comma separeted and storing into p list
print(p)  #printing the binarry number which are divisible by 5 after coverting to the dicimal number