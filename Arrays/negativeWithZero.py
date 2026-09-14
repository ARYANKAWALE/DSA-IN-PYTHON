arr = [3,-5,2,-6,1,-2]
position = 0
for i in arr:
    if i < 0:
        arr[position] = 0
    position+=1
print(arr)