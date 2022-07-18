# Given an array of numbers, write a function that returns a new array that contains all numbers from the original array that are less than 100.

input = [99, 101, 88, 4, 2000, 50]
# Output: [99, 88, 4, 50]


def less_than(input):
    new_arr = []
    for i, input in enumerate(input):
        if i < 100:
            new_arr.append(i)


print(less_than(input))
