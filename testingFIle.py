# Define a function to square a number
def square(x):
    return x ** 2

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use the map function to apply the square function to each element in the list
squared_numbers = map(square, numbers)

# Convert the result to a list (as map returns an iterator)
squared_numbers_list = list(squared_numbers)

# Print the result
print(squared_numbers)
