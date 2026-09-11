arr = [-1,0,1,2,-1,4]
arr.sort()
result = []
for i in range(len(arr)-2):
    if i>0 and arr[i] == arr[i - 1]:
        continue
    left, right = i + 1, len(arr) - 1
    sum = -1 * arr[i]
    while left < right:
        s = arr[left] + arr[right]
        if(s == sum):
            result.append([arr[i], arr[left], arr[right]])
            left +=1
            right -= 1
            while(left < right and arr[left] == arr[left - 1]):
                left += 1
            while(left < right and arr[right] == arr[right + 1]):
                right -= 1
        elif s< sum:
            left+=1
        else:
            right-=1
print(result)
