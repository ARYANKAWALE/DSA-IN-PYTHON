rev = "aryan"
left = 0
right = len (rev) - 1
arr = list(rev)
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left+=1
    right-=1
print("".join(arr))