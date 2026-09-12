def twoSum(nums,target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return "Not Found"

print(twoSum([-1,0,1,2,-1,4],3))