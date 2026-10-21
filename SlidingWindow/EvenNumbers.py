arr = [1,2,3,4,5]
k = 2
low = 0 
high = k - 1
n = len(arr)
res = []
while high < n:
    even_count = []
    current_pos = low
    while current_pos <= high:
        if arr[current_pos] % 2 == 0:
            even_count = even_count + [arr[current_pos]]
        current_pos+=1
        if even_count != [] and even_count not in res:
            res = res + [even_count]
    low+=1
    high+=1
print(res)