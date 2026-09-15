arr = [1]
first = 0
second = 1
is_increasing = True
if len(arr) < 2:
    is_increasing = False
else:
    while second < len(arr):
        if arr[first] >= arr[second]:
            is_increasing = False
        first+=1
        second+=1
print(is_increasing)