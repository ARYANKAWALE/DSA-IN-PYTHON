arr = [1,2,3,4,5]
n = len(arr)
prev = [0] * n
for i in range(n):
    curr_sum = 0
    for j in range(i+1):
        curr_sum = curr_sum + arr[j]
    prev[i] = curr_sum
print(prev)