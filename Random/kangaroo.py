A = input("Enter the inputs: ").split(" ")
s1 = int(A[0])
s2 = int(A[1])
j1= int(A[2])
j2= int(A[3])

def jumping(s1,s2,j1,j2):
    k1= []
    k2 = []
    s = "NO"
    if s1>=0 and s1<s2 and s2<=10000 and j1>=1 and j1<=10000 and j2 >= 1 and j2<=10000:
        jf = s1 + j1
        jd = s2 + j2
        for i in range(10000000000):
            jf+=j1
            k1.append(jf)
            jd +=j2
            k2.append(jd)
        for i in range(len(k2)):
            if k1[i] is k2[i]:
                s = "YES"
                break
    print (s)

jumping(s1,s2,j1,j2)
