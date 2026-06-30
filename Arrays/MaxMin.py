def minMax(arr):
    if len(arr) == 0:
        return None,None

    max_val = arr[0]
    min_val = arr[0]
    
    for i in range(1,len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        elif arr[i] < min_val:
            min_val = arr[i]

    return max_val,min_val

nums = [3, 5, 4, 1, 9]
maximum, minimum = minMax(nums)
print(f"Max Element: {maximum}, Min Element: {minimum}")