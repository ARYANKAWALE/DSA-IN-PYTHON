num = [2,5,6,7,8,9]
smallest = num[0]
greatest = num[0]
for i in num:
    if i < smallest:
        smallest = i
    if i > greatest:
        greatest =i
        
print("smallest number is:",smallest, "And the greatest is:",greatest)