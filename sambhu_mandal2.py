k=int(input("enter an integer"))
t=0
for i in range(2,7):
    if k%i ==0:
        print(f"{k//i}")
        t+=k//i
print(f"total bitcoins should be :{t}") 