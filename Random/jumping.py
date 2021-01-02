def jmpn(n, dj):
    d= 0
    if n >=2 and n <=100 and dj[0]== 0:
        for i in range(len(dj)):
            if dj[i] == 1 and dj[i-1] != 1:
                d+=1
            if dj[i] == 0 and dj[i-1] == 0 and i>0 and i!= len(dj):
                d+=1
    else:
        print("")
        
    print (d)

def jmp (n, d):
    a = 0
    z= 0
    if n >=2 and n <=100 and d[0]== 0:
        for i in range(len(d)):
            if d[i] == 0:
                z += 1
            if d[i] == 1:
                a+=1
                a+=int(z/2)
                z = 0
    return a






x = int(input("enter number of inputs: "))

app = []
for i in range(x):
    ap = int(input("enter number: "))
    if ap == 1 or ap==0:
        app.append(ap)
    else:
        ap = int(input("enter number: "))
        
print(app)
jmpn(x, app)
