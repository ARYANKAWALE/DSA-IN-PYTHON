arr = [1,2,4,6,9,4,6,2,3,5]
arr.sort()
left = 0
right = 1
while right < len(arr):
    if arr[left] != arr[right]:
        left+=1
        arr[left] = arr[right]
    
    right += 1
print(arr[:left + 1])