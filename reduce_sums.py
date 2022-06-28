# Write a function that returns the sum of all numbers in a given array.

# NOTE: Do not use any built-in language functions that do this automatically for you.

# Input: [1, 2, 3, 4]
# Output: 10

# Explanation: (1 + 2 + 3 + 4) = 10

def calculate_sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


arr = [1, 2, 3, 4]
res = calculate_sum(arr)
print(res)
