arr = [5,7,6,9,2,1]
def FindLarge(arr):
    max = arr[0]
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max
print(FindLarge(arr))