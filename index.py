# import array
# import array as arr
from array import *

# val = array.array('i',[1,2,3,4,5,6,7,8,9])
# val = arr.array('i', [1,2,3,4,5,6,8,9])


val = array('i',[1,2,3,4,5,6,7,8,9])
# val = array('d',[1,2,3,4,5,6,7,8,9.5])
# val = array('u',['a','b','c','d','e','f','g','f'])
# print(val)

# for i in range(0,6):
# for i in range(0,len(val)):
    # print(val[i])
    # print(val[i],end=" ")

# print('\n')

# for x in val:
#     # print(x)
#     print(x, end=",")

# print('\n')

# print(val.typecode)

# print('\n')

# val.reverse()

# for i in range(0,len(val)):
#     print(val [i], end=" ")

# print('\n')

# val.insert(1,50)
# val.append(60)
# val[2]=200
# val.remove(1)
# val.pop()
# val.index(5)

# for i in range(0,len(val)):
#     print(val [i], end=" ")

# copyArray = array(val.typecode ,(x*2 for x in val))

# copyArray.pop(3)

# for i in range(0,len(copyArray)):
#     print(copyArray [i], end=" ")


# abc = val[2:5]
# abc = val[2:-3]
# abc = val[::-1]
# for i in range(0,len(abc)):
#     print(abc[i],end=' ')


# arr = array('i',[])
# n = int(input("Enter a Number:"))
# for i in range(0,n):
#     arr.append(int(input('Enter next Number:')))
    
# for x in arr:
#     print(x,end=" ")



arr = array('i',[4,7,23,75,256])

i = arr.index(23)
print(i)

