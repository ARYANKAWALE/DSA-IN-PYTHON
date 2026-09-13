arr = [10, 5, 8, 20, 15]

# Start both tracking pointers at the first element
first = second = arr[0]

for num in arr:
    if num > first:
        second = first  # Old largest becomes second largest
        first = num     # Current becomes the new largest
    elif num > second and num != first:
        second = num    # Update second largest if it's in between

print(second)  # Output: 15
