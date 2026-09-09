arr = [1,1,1,2,2,3,3,3]
left = 0
right = len(arr) -1
target = 4
result = []
while left < right:
    current_sum = arr[left] + arr[right]
    if(current_sum == target):
        result.append([arr[left],arr[right]])
        left +=1
        right-=1
        while left < right and arr[left] == arr[left - 1]:
            left += 1
        while left < right and arr[right] == arr[right + 1]:
            right -= 1
    elif(current_sum < target):
        left+=1
    else:
        right-=1
print(result)