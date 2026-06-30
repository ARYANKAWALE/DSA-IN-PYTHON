nums = [1,2,3,2,1]
left = 0
right = len(nums) - 1
is_palindrome = True
while left < right:
    if nums[left] == nums[right]:
        left += 1
        right -= 1
    else:
        is_palindrome = False
        break
print(is_palindrome)
