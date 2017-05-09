import time

list1 = [1, 3, 4, 5]
list2 = [2, 4, 5, 6, 8]

def linear_merge(list1, list2):
      # +++your code here+++
    for x, y in map(list1, list2):
          print x, y

# linear_merge(list1, list2)

numbers = [5, 10, 15, 20, 25, 30]

print(time.time())

for c in range(0, 10):
    sum = 0
    for i in map(lambda v: v + 20, numbers):
        sum += i

print(time.time())

for c in range(0, 10):
    sum = 0
    for v in numbers:
        sum += (v + 20)

print(time.time())
