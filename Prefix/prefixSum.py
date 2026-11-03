# This Equation Worst Time Complexity is O(n^2)
# arr = [1,2,3,4,5]
# n = len(arr)
# pre = [0] * n
# for i in range(n):
#     curr_sum = 0
#     for j in range(i+1):
#         curr_sum = curr_sum + arr[j]
#     pre[i] = curr_sum
# print(prev)


# This Equation Worst Time Complexity is O(n)
arr = [1,2,3,4]
n = len(arr)
pre = [0] * n
pre[0] = arr[0]
for i in range(1,n):
    pre[i] = pre[i - 1] + arr[i]
print(pre)
