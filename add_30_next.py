l=[1,3,5,7,9,11,13,15]
for i in l:
    for j in l:
        for k in l:
            c=(i+j+k)
            if c==30:
                print(f"{i},{j},{k}")
            else:
                print("error")
            