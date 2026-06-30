nums = [4,5,4,7,4,9]
target = 4
count = 0
for i in nums:
    if i == target:
        count = count + 1
        pass
print("The count of",target,"is",count)