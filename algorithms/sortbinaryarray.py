# sort binary array in linear time
# Input =  { 1, 0, 1, 0, 1, 0, 0, 1 }
# Output = { 0, 0, 0, 0, 1, 1, 1, 1 }

import random
import time

def sort(input):
    numberofzeros = 0
    for index in input:
        if index == 0:
            numberofzeros += 1
    zeros = [0] * numberofzeros
    ones = [1] * (len(input) - numberofzeros)
    return zeros + ones

def anothersort(input):
    left = 0
    right = len(input) - 1
    while (left < right):
        while (input[left] == 0 and left < right):
            left += 1
        while (input[right] == 1 and left < right):
            right -= 1
        if (left < right):
            input[left] = 0
            input[right] = 1
            left += 1
            right -= 1

inputdata = [1, 0, 1, 0, 1, 0, 0, 1, 0, 1]

starttime = time.time()
anothersort(inputdata)
endtime = time.time()

print inputdata
print("--- %s seconds ---" % (time.time() - starttime))


