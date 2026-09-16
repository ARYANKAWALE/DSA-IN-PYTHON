arr = "nayan"
left = 0
right = len (arr) - 1
is_palindrome = False
while left < right:
    if arr[left] == arr[right]:
        left+=1
        right-=1
        is_palindrome = True
    else:
        is_palindrome = False
        break
print(is_palindrome)