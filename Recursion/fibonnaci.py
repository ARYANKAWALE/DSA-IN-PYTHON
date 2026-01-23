# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)
# print(fib(6))

def fib(n:int)->int:
    ans = [0,1]
    for i in range(2,n+1):
        ans.append(fib(i-1) + fib(i-2))
    return ans[n]
print(fib(6))