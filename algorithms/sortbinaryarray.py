# sort binary array in linear time
# Input =  { 1, 0, 1, 0, 1, 0, 0, 1 }
# Output = { 0, 0, 0, 0, 1, 1, 1, 1 }

def sort(input):
    numberofzeros = 0
    for index in input:
        if index == 0:
            numberofzeros += 1
    zeros = [0] * numberofzeros
    ones = [1] * (len(input) - numberofzeros)
    return zeros + ones

print sort([1, 0, 1, 0, 1, 0, 0, 1])


