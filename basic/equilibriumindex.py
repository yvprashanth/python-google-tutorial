# For an array A consisting n elements,
# index i is an equilibrium index if sum of elements of sub-array A[0..i-1]
# is equal to the sum of elements of sub-array A[i+1..n-1]

def calculate(a):
    sum = 0
    for index in a:
        sum += index
    right = 0
    reversedarray = [x for x in a[::-1]]
    for idx, val in enumerate(reversedarray):
        if right == sum - (val + right):
            return idx
        right += val
        
answer = calculate([0, -3, 5, -4, -2, 3, 1, 0])
print(answer)
        