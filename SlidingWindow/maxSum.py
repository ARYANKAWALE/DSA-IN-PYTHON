arr = [100,200,300,400]
low = 0 
high = 1
window_sum = 0
n = len(arr)
res = 0
for i in range(low, high + 1):
    window_sum = window_sum + arr[i]
while high < n:
    res = max(res,window_sum)
    low+=1
    high+=1
    if high == n:
        break
    window_sum = window_sum - arr[low - 1]
    window_sum = window_sum + arr[high]
print(res)