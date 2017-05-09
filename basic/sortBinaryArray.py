# Given an binary array, sort it in linear time and constant space. Output should print contain all zeroes followed by all ones
# Input: { 1, 0, 1, 0, 1, 0, 0, 1 }
# Output: { 0, 0, 0, 0, 1, 1, 1, 1 }

def calculate(a):
    noofzeros = 0
    for i in a:
        if i == 0:
            noofzeros += 1
    return noofzeros
    