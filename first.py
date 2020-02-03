print('hello')
print("hello world")
print("hello world 'world'")
print('hello world"world"')
print("first line \nsecond line")
myint=7
print(myint)
myfloat=7.0
print(myfloat)
myfloat=float(7)
print(myfloat)
mystring='hello'
print(mystring)
print("boton\nsambhu\nsubham")
one=1
two=2
hello="hello"
print(one+two)
print(2+3)
print("this is double slash \\\\")
print("This is \\\\ double back slash")
print("This are /\\/\\/\\/\\/\\ mountains")
print("he is \t awesome")
print("\\\" \\n \\t \\'")
print("\\")
print("\U0001F481")
#exercise 1
#a=float(input("enter first number"))
#b=float(input("enter second number"))
#c=float(input("enter third number"))
#d=(a+b+c)/3
#print("the average is {}".format(d))
#print(f"the average is {d}")
#end
#multi input with a single line
#a,b,c=(input("enter three numbers").split(","))
#d=(int(a)+int(b)+int(c))/3
#print("the average is {}".format(d))
#print(f"the average is {d}")
#end
#input one string and print it revarse order
#name=input("enter your name")
#print(name[::-1])
#end
#string methods
#name,char=input("enter a name and a character").split(",")
#print(len(name))
#print(name.count(char))
#end
#if-else statement
#num=20
#newnum=int((input("enter a number")))
#if num==newnum:
   # print("you win!!!")
#else:
    #if newnum > num:
        #print("number is too high")
    #else:
        #print("number is too low")
#end 
# watch coco  
#name,age=input("enter your name and age").split(",")
#age=int(age)
#if (name[0]=='a' or name[0]=='A') and age >=10:
    #print("you can watch that movie")
#else:
    #print("you are not allowed to watch the movie")
#end  
# while loop
#i=1
#sum=0
#while i<=10:
    #sum=sum+i
    #i+=1
#print("sum is "+str(sum))    
#end 
# sum of digits of a number
#number=input("enter a number more than one digit")
#i=0
#sum=0
#while i<len(number):
    #sum=sum+int(number[i])
    #i+=1
#print("total is:"+str(sum))
#end  
# count the character in a given string
#name=input("enter your name")
#i=0
#while i<len(name):
    #c=name.count(name[i])
    #print(f"{name[i]} : {c}")
    #i+=1
# end  
# for loop
#name=input("enter your name")
#temp=""
#for i in range(len(name)):

    #if name[i] in temp:
        #pass
    #else:

        #print(f"{name[i]} : {name.count(name[i])}")
    #temp=temp + name[i]
    #print(str(i)+ temp)
   
       
# end 
#guess number game
#import random
#number =random.randint(1,100)
#for i in range(100):
    #uinput=input("guess a number 1 to 100")
    #if number == int(uinput):
        #print(f"you win!!!you take {i} times to win")
        #break
    #else:
        #if int(uinput) > number:
            #print("too high")
        #else:
            #print("too low")    
        #continue   
#end
#for loop with string
#name,char=input("enter your name and one character").split(",")
#for i in name:
    #if i==char:
        #temp+=1
#print(f"the {char} is {temp} times in this name {name}")        

#end
#function for print last char of a name
#def last_char(name):
    #for i in name:
        #return (name[len(name)-1])
#char=last_char(input("enter your name"))
#print(f"last character of the given name is {char}")  
#end
# function for odd even
#def odd_even(number):
    #if number % 2== 0:
        #print("even")
    #else:
        #print("odd")
#odd_even(int(input("enter a number")))            
# end  
# function for bigger number between two number
#def bigger_number(num1,num2):
    #if int(num1) > int(num2):
        #print("num1 is greater")
    #else:
        #print("num2 is greater")
#bigger_number(input("enter first numbers"),input("enter second number"))            
# end 
# function for greatest number among three numbers
#def greatest(num1,num2,num3):
    #if num1 >num2 and num1 >num3:
        #print("num1 is greatest")
    #elif num2 >num1 and num2 >num3:
        #print("num2 is greatest")
    #else:
        #print("num3 is greatest")
#greatest(int(input("enter first number")),int(input("enter second number")),int(input("enter third number")))                
# end  
# function within function
#def bigger_number(num1,num2):
    #if int(num1) > int(num2):
        #return num1
    #else:
        #return num2
#def greatest(a,b,c):
    #bi=bigger_number(a,b)
    #bii=bigger_number(bi,c)
    #return bii 
#print(greatest(int(input("enter first number")),int(input("enter second number")),int(input("enter third number"))))    

# end 
#palindrom or not
#def is_palindrom(something):
    #temp=""
    #for i in range(len(something)-1,-1,-1):
        #temp=temp + something[i]    
    #return temp 
        
#a=input("enter something")
#temp1=is_palindrom(a)
#if a == temp1:
    #print("given item is palindrom")
#else:
    #print("not palindrom")

#end
#fibonacci series
#def fibo(how_many):
    #f1=0
    #f2=1
    #if how_many ==1:
        #print("0")
    #elif how_many ==2:
        #print("0\n")
        #print("1\n")
    #else:
        #print("0 \n")
        #print("1 \n")
        #for i in range(how_many-2):
            #f3=f1+f2
            #print(f"{f3}\n")
            #f1=f2
            #f2=f3
#fibo(int(input("enter a number for fibonacci series:")))     
#list
#print(list1[-1])
#print(list1[0:3:2]) 
#list1[1]='Two'# to change the particular list item
#print(list1)  
#list1[:3]=['one','two',"name1"]# to change the more than one item at a time
#print(list1)
#list3=['mango','banana']
##list4=['orange','apple']
#list3.extend(list4)
#print(list3)
#list3.append(list4)
#print(list3)  
#end
#function with list where function returns the square of the list items
#numbers=list(range(1,21))
#def square(l):
    #s=[]
    #for i in l:
        #s.append(i*i)
    #return s
#print(square(numbers)) 
#end
#function with list where function returns the reverse of a giving list
#list1=list(range(1,101))
#def rev(l):
    #r=[]
    #for i in range(len(l)-1,-1,-1):
        #r.append(i)
    #return r
#print(rev(list1)) 
#end
#function with list where all the elements will be reverse
#def reverse_string(l):
    #list1=[]
    #for i in l:
        #list1.append(i[ : :-1])
    #return list1
#n=input("enter how many string in list you want")
#list2=[]
#for j in range(int(n)):
    #list2.append(input(f"enter {j}th string"))
#print(reverse_string(list2))            
#end
#function with list for filtering odd and even
#def odd_even(l):
    #list1=[]
    #list2=[]
    #list3=[]
    #for i in l:
        #if i%2 ==0:
            #list1.append(i)
        #else:
            #list2.append(i)
    #list3.append(list1)
    #list3.append(list2)
    #return list3
#list4=list(range(1,101))
#print(odd_even(list4))


#end
#function with list where two lists are passing as arguments
#def common(l1,l2):
    #fin=[]
    #for i in l1:
        #for j in l2:
            #if j==i:
                #fin.append(j)
    #return fin
#list1=list(range(1,20))
#list2=list(range(10,25))
#print(common(list1,list2))

#end
#function returns two values as a tuple
def func(int1,int2):
    add=int1 + int2
    mult=int1 * int2
    return add,mult
addition,multiply=func(2,3)
print(addition) 
print(multiply)   
#end
#numbers=tuple(range(1,11))
#print(numbers)
#list1=list(numbers)
#print(list1)
#n=str(list1)
#print(n)
#print(type(n))
def power(c,y):
    p=c**y
    return p
a=1 #input("enter number ")
b= 1 #input("enter exponent")
s=float(a)
t=int(b)
z=power(s,t)
print(z) 


list1=['sambhu','mandal']
def rev(l):
    list2=[a[ : :-1] for a in l]
    return list2
d=rev(list1)
print(d)  


def example1(num,*args):
    list3=[i**num if(len(args)>0) else print("u didn't pass the *args") for i in args]
    if len(list3)>0:
        return list3
    else:
        print("u  didn't pass *argssss")    
    
    #if len(args)>0:
        #list1=[]
        #for i in args:
            #list1.append(i**num)
        #return list1
    #else:
        #print("u didn't pass the *args")
list2=[1,2,3,4]        
print(example1(3,*list2))   
a="sambhu"
b=10
print(f"age of {a} is {b}")


names=['sambhu','mandal','khalia','ayan']
string1='samb'
def posi(l,s):
    for pos,name in enumerate(names):
        if name == s:
            print(f"{pos}------>{s}")
            break
        else:
            print('-1')
posi(names,string1)                

names1=['sambhu','mandal','khalia']
string2='sambhu'
def possi (l,s):
    for pos,name in enumerate (l):
        if s== name:
            return pos
        return -1
po=possi(names,string2)
print(po)


num=[1,2,3,4,5,6]
num_iter=iter(num)
print(next(num_iter))
print(next(num_iter))

#def prac1(l1,l2):
    #t1,t2,t3=list(zip(l1,l2))
    #for i in t1:
        #f1=0
        #f1+=i
    #for j in t2:
        #f2=0
        #f2+=j
    #for k in t3:
        #f3=0
        #f3+=k
    #return f1/3,f2/3
#numb1=[1,2,3,4]
#numb2=[5,6,1,2]
#numb3=[4,2,5,1]
#r1,r2=prac1(numb1,numb2)
#print(r1,r2) 


students = {
    'harshit': { 'score':90,'age':24},
    'mohit' : { 'score':75,'age' :19},
    'rohit' : { 'score':76, 'age':23}
}
print(max(students,key = lambda item :students[item]['score']))


namess=['sambhu:12','mandal:10','khalia:11']
print(sorted(namess))
print(namess)
namess.sort()
print(namess)


class Laptop:
    def __init__(self,brand_name,price):
        self.brand_name=brand_name
        self.price=price
l1=Laptop('dell',35000)
print(f"{l1.brand_name} : {l1.price}")   

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
p1=Person('sambhu','mandal',26) 
p2=Person('soven','mandal',30)
print(f"{p1.first_name} {p1.last_name} : {p1.age}") 
print(f"{p2.first_name} {p2.last_name} : {p2.age}")      


#method with class:
class Laptop1:
    def __init__(self,brand_name,price):
        self.brand_name=brand_name
        self.price=price
    def percentage_off(self,p):
        p1=self.price - ((self.price * p)/100)
        return p1


l1=Laptop1("dell",40000)
l2=Laptop1("lenovo",30000)
l3=Laptop1("hp",35000)
print("-------ORIGINAL PRICE-------")
print(f"{l1.brand_name}   : {l1.price}")
print(f"{l2.brand_name}   : {l2.price}")
print(f"{l3.brand_name}   : {l3.price}")
print("---------DISCOUNT PRICE--------")
print(f"{l1.brand_name}   : {l1.percentage_off(40)}")
print(f"{l2.brand_name}   : {l2.percentage_off(40)}")
print(f"{l3.brand_name}   : {l3.percentage_off(40)}")


#user adult or not:
class Person1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def is_adult(self):
        if self.age > 18:
            return "true"

a1=Person1('sambhu',26)
a2=Person1('ayan',17) 
if a1.is_adult() == "true":
     print(f"{a1.name} is adult")
else:
     print(f"{a1.name} is not adult")
if a2.is_adult() == "true":
     print(f"{a2.name} is adult")
else:
     print(f"{a2.name} is not adult")





class Laptops:
    dis=10
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def disc(self):
        return self.price - ((self.price * self.dis)/100) 
lap1=Laptops("Dell",50000)
lap2=Laptops("HP",40000)
lap3=Laptops("Lenovo",30000)
lap2.dis=50
print(f"{lap1.brand} : {lap1.disc()}")
print(f"{lap2.brand} : {lap2.disc()}")
print(f"{lap3.brand} : {lap3.disc()}")
print(lap2.__dict__)


#inheritance
class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def fullname(self):
        return f"{self.brand} {self.model}"
    def makecall(self,number):
        return f"calling {number}..."

class Smartphone(Phone):
    def __init__(self,brand,model,price,ram,camra,storage):
        super().__init__(brand,model,price) 
        self.ram=ram
        self.camra=camra
        self.storage=storage

p1=Phone("nokia","1100",1000)
print(p1.fullname())
print(p1.makecall("8217869531"))
p2=Smartphone("samsung","c7pro",28000,"4GB","16","64GB")    
print(p2.fullname())
print(p2.makecall("9800751445"))  
print(p2.brand)                     



k=int(input("enter an integer"))
t=0
for i in range(2,7):
    if k%i ==0:
        print(f"{k//i}")
        t+=k//i
print(f"total bitcoins should be :{t}") 


#exception handling
def devide(a,b):
    return a/b

while True:
    try:
        a=int(input ('enter first number'))
        b=int(input('enter second number'))
    except ValueError:
        print('maybe u entered string instead of integer')
    except ZeroDivisionError:
        print('don\'t divide by zero to any number')  
    except TypeError:
        print('u should enter integer only')
    else:
        print(devide(a,b))
        break
        
    finally:
        print('finally block...')
           

#fibonacci number match
fib=[0,1]
a=0
b=1
for i in range(100):
    c=a+b
    fib.append(c)
    a=b
    b=c
print(fib) 
fibon=[]
def is_part_of_series(*args):
    for i in args:
        if i==0:
            fibon.append(0)
        elif i==1:
            fibon.append(1)
        else:
            l=((2*(i-1)) -(2*(i-2))) 
            fibon.append(l)
    return fibon
number=[0,1,0,2,3,5,11]     
p= is_part_of_series(*number)    
print(p)
flag=1
for i in fibon:
    if i in fib:
        flag=flag
        continue
    else:
        flag=0
        break
if flag==1:
    print("this list is not the part of series")
else:
    print("this is not the part of series")        



    


