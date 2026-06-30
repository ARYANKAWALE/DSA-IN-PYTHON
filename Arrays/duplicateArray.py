arr = [1,1,2,3,3,4,5,6]

start = 0
for i in range(len(arr)):
    if arr[i] != arr[start]:
        start +=1
        arr[start] = arr[i]
start+1
print("The array without duplicate numbers is:",arr[:start +1])