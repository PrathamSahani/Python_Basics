import random

# Generate a random integer between a given range (inclusive)
random_integer = random.randint(1, 100)
print("Random Integer:", random_integer)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random Float:", random_float)

# Generate a random floating-point number within a specified range
random_float_range = random.uniform(1.0, 10.0)
print("Random Float in Range:", random_float_range)

# Generate a random element from a sequence (e.g., a list)
my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)
print("Random Element from List:", random_element)

# Shuffle the elements of a sequence in-place (e.g., a list)
random.shuffle(my_list)
print("Shuffled List:", my_list)

# Generate a random sample of elements from a sequence without replacement
sample = random.sample(my_list, 5)
print("Random Sample:", sample)
