nums = [3,5,6,2,8,4,1]
left = 0
right = len(nums) - 1
while left < right:
    nums[left],nums[right] = nums[right],nums[left]
    left = left + 1
    right = right - 1
print(nums)