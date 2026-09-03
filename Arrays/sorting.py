def twoSum(arr,target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while(left < right):
        current_sum = arr[left] + arr[right]
        if (current_sum == target):
            return [left,right]
        elif (current_sum < target):
            left += 1
        elif (current_sum > target):
            right -= 1
    return "Empty error"
arr = [5,8,7,2]
target = 23
print(arr , "unsorted")
print(arr, "sorted")
print(twoSum(arr,target))