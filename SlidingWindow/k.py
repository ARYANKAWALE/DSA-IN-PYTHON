arr = [3,8,2,5,7,6,12]
curr = 0
w=4
for i in range(w):
    curr += arr[i]

maxx = curr
n =len(arr)
for i in range(1, n - w + 1):
    curr = curr - arr[i - 1] + arr[i + w - 1]
    if(curr > maxx):
        maxx = curr
print(maxx)