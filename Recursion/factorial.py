# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(4))

num = 5
fact=1
for i in range(1,num+1):
    fact = fact*i
print(f"Factorial of {num} is {fact}")  