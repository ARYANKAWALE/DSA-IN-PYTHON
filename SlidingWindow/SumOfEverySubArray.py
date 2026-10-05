arr = [1,2,3,4,5]
k = 3
low = 0
high = 2
result = []
n = len(arr)
maxVal = float('-inf')
while high < n:
    current_sum = sum(arr[low:high + 1])
    maxVal = max(maxVal,current_sum)
    result.append(maxVal)
    low+=1
    high+=1
    
print(result)