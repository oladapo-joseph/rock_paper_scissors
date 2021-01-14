def grad(s):
    if len(s)<=60:
        for i in s:
            d=i
            if d>=38 and d<=100:
                jk = int(d/5)
                f = ((jk+1)*5) - d
                if f <3:
                    d= d + f
                    print (d)
                else:
                   print(d)
            else:
                print(d)
    

s = int(input("number of grades: "))
j =[]
for _ in range(s):
    sd = int(input("enter grades: "))
    j.append(sd)
grad(j)

    
