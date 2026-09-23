arr = [1,2,4,4]
target = 4
low = 0 
high = 0
current_sum=0
n = len(arr)
res = n + 1
while high < n:
    current_sum = current_sum + arr[high]
    while current_sum >= target:
        lenght = high - low + 1
        if lenght < res:
            res = lenght
        current_sum = current_sum - arr[low]
        low+=1
    high+=1
if res == n + 1:
    res = 0
print(res)
