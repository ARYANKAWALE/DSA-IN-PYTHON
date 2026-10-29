arr = [-2,1,-3,4,-1,2]
bestending = arr[0]
ans = arr[0]
for i in range(len(arr)):
    v1 = bestending + arr[i]
    v2 = arr[i]
    bestending = max(v1,v2)
    ans = max(ans,bestending)
print(ans)