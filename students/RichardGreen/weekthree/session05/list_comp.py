'''In this exercise, using a list comprehension, return the number of
even ints in the given array.'''


def count_evens(nums):
    ''' This function uses comprehensions and determines the even
    numbers in a sequence. Arguments: a list of numbers'''
    # Create an empty string to contain the even numbers
    results = ''
    results = [x for x in nums if x % 2 == 0]

    # Print the length/number of Even numbers in our string"
    print len(results)

if (__name__ == "__main__"):

    # Lets create a list of 50 integers
    x = range(50)

    # Lets print those values that are even
print count_evens(x)

# Lets run the unit tests that were provided in the exercise
print count_evens([2, 1, 2, 3, 4])

print count_evens([2, 2, 0])

print count_evens([1, 3, 5])
