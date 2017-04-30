import random
from sets import Set

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)/2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

arr, i = Set(), 0
while(i < 100):
    i += 1
    if i in arr:
        continue
    else:
        arr.add(random.randint(0, 100))

print quicksort(list(arr))
