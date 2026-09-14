arr = [2,8,5,3,2,4]
postion = 0
for i in arr:
    if (i%2==0):
        arr[postion] = 0
    postion+=1
print(arr)