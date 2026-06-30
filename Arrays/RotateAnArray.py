arr = [5,4,3,2,1]
left = len(arr) - 1
last_element = arr[left]
for i in range(left -1, -1, -1):
    arr[i+1] = arr[i]
arr[0] = last_element
print(arr)