arr = [3,4,6,1,7,9,1]
def SecondLargest(arr):
    largest = arr[0]
    secondLargest = arr[0]
    for i in range(len(arr)):
        if arr[i] >  largest:
            secondLargest = largest
            largest = arr[i]
        elif arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    return secondLargest
print(SecondLargest(arr))