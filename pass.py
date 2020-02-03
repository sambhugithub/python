import re  #importing re for using the search()method in program
def pas(s): #definition of pas with one string which is the password giving by user
    x=True
    while(x): #loop
        #for condition checking purpose
        if (len(s)<6 or len(s)>12):
            break
        elif not re.search("[a-z]",s):
            break
        elif not re.search("[0-9]",s):
            break
        elif not re.search("[A-Z]",s):
            break
        elif not re.search("[$#@]",s):
            break
        elif re.search("\s",s):
            break
        #after check all the condition which are all false then we can say this is the valid password and we make x=False 
        else:
            return f"your password is valid"
            x=False
            break
    #still if x =True then any of the condition was satishfied in while block then the password should not be valid     
    if x:
        print(" your password is Not a Valid Password")

print(pas(input("enter a password")))   #function call with taking input from user 