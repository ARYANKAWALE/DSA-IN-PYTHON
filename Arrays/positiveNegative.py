arr = [-1,4,2,-5,2,8,6,-2]
positive = []   
negative = []
for num in arr:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)
print("postive:",positive)
print("negative:",negative)