l=[1,3,5,7,9,11,13,15]
r=[]
for i in l:
    for j in l:
        print(f"{i},{j}")
        p=(i+j)
        q=(30-p) 
        r.append(q)
print(r)       
for i in r:
    if i in l:
        print(i)
    else:
        print("error")    
             

