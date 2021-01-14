y = int(input("give a finite number of of entries: "))
#x = input("enter a number to add 1 to it and express it in a list: ")
arr = []
count = 0
while count < y:
    x = int(input("enter a number to add 1 to it and express it in a list: "))
    arr.append(x)
    count = count + 1
#del arr[count]
print (arr)

x = 0
y = 0
for i in range(len(arr)):
    if i!= 0:
        if arr[i] == 0:
            x = x +1
            if i>1 and arr[i-1]== 0 and arr[i-2] ==0:
                x = x - 1
        elif arr[i] == 1:
             x = x 
    print ("at ", arr[i], "we count ",x)
    print ("round", i)
print (x)
    
    
