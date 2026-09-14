arr = [3,5,1,9,6,0]
found_zero = False
for i in arr:
    if i == 0:
        found_zero = True
        break
if found_zero:
    print("This array has zero")
else:
    print("This array doesn't have zero")