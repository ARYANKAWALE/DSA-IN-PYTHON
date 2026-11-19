arr = [100,200,300,400]
low = 0 
high = 1
window_sum = 0
n = len(arr)
res = 0
for i in range(low, high + 1):
    window_sum = window_sum + arr[i]
print(window_sum)