num = [2,5,6,7,8,9,10]
smallest = num[0]
greatest = num[0]
sum = 0
for i in num:
    if i < smallest:
        smallest = i
    elif i > greatest:
        greatest =i
    sum+=i
    
print("smallest number is:",smallest, "And the greatest is:",greatest)
print("The sum of all number is:",sum)