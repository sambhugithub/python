k=int(input("enter an integer"))
t=0
for i in(2,5):
    if(k%i==0):
        t+=k/i
print(f"total bitcoins should be :{t}")        
