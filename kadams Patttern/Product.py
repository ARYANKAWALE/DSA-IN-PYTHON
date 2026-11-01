arr = [-2,3,-4]
bestending = arr[0]
maxending = arr[0]
minending = arr[0]
res = arr[0]
for i in range(1,len(arr)):
    v1 = arr[i]
    v2 = minending * arr[i]
    v3 = maxending * arr[i]
    maxending = max(v1, max(v2,v3))
    minending = min(v1,min(v2,v3))
    res = max(res,max(maxending,minending))
print(res)