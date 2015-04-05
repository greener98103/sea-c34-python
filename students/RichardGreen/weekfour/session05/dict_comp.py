'''Dictionary Comprehensions Lab'''
'''Richard Green'''


my_dict = {"name": 'Rich',
           "city": 'Seattle',
           "desert": 'Chocolate',
           "drink": 'espresso',
           "number": 'Four',
           "time": 'Three hours'}

# Print the dict by passing it to a string format method

story = ('{name} is from {city} and loves {desert}, especially after {number}'
         'shots of {drink} and {time} of sleep')

story_formated = story.format(name=my_dict["name"],
                              city=my_dict["city"],
                              desert=my_dict["desert"],
                              number=my_dict["number"],
                              drink=my_dict["drink"],
                              time=my_dict["time"]
                              )
# Print the dict by passing it to a string format method

print story_formated


# Using a list comprehension, build a dictionary of numbers from
# zero to fifteen and the hexadecimal equivalent (string is fine).

hex_list_dict = dict([(i, hex(i)) for i in range(0, 16)])

print hex_list_dict
print type(hex_list_dict)

# Do the previous entirely with a dict comprehension. should be a one liner
hex_dict = {i: hex(i) for i in range(0, 16)}

print hex_dict
print type(hex_dict)

# Using the dictionary from item 1: Make a dictionary using the same keys
# but with the number of a s in each value. You can do this either by editing
# the dict in place, or making a new one. If you edit in place, make a copy
# first

# Make a new dictionary and use the same keys to built a dict with the number
# of a 's'
my_a_dict = dict()

print "The number of [a]s in the dictionary are:"

my_a_dict = {k: v.count('a') for k, v in my_dict.iteritems()}

print my_a_dict


# Create sets s2, s3 and s4 that contain numbers from zero through twenty,
# divisible 2, 3 and 4. Do this with one set comprehension for each set.

s2 = set()
s3 = set()
s4 = set()


set(s2.add(x) for x in range(0, 21) if x % 2 == 0)
set(s3.add(x) for x in range(0, 21) if x % 3 == 0)
set(s4.add(x) for x in range(0, 21) if x % 4 == 0)

print s2
print s3
print s4

# create a sequence that holds all three sets
seq_sets = [s2, s3, s4]
# loop through that sequence to build the sets up so no repeated code
# Extra credit: do it all as a one-liner by nesting a set comprehension
# inside a list comprehension. (OK, that may be getting carried away!)

seq_sets = [{i for i in range(0, 21) if not i % j} for j in range(2, 5)]

print s2
print s3
print s4
