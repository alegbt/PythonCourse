# Uncomment the commented lines of code below and complete the list comprehension logic

# The floats variable should store the floating point values
# for each string in the values list.
values = ["3.14", "9.99", "567.324", "5.678"]
floats = [float(v) for v in values]
print(floats)

# The letters variable should store a list of 5 strings.
# Each of the strings should be a character from name concatenated together 3 times.
# i.e. ['BBB', 'ooo', 'rrr', 'iii', 'sss']
name = "Boris"
letters = [c*3 for c in name]
print(letters)

# The 'lengths' list should store a list with the lengths
# of each string in the 'elements' list
elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
lengths = [len(w) for w in elements]
print(lengths)


# Declare a destroy_elements function that accepts two lists.
# It should return a list of all elements from the first list that are NOT contained in the second list.
# Use list comprehension in your solution.
#
# EXAMPLES
# destroy_elements([1, 2, 3], [1, 2])      => [3]
# destroy_elements([1, 2, 3], [1, 2, 3])   => []
# destroy_elements([1, 2, 3], [4, 5])      => [1, 2, 3]



def destroy_elements(first, second):
    return [element for element in first if element not in second]

print(destroy_elements([1,2,3], [4,5,1,2]))





# Declare a destroy_elements function that accepts two lists.
# It should return a list of all elements from the first list that are NOT contained in the second list.
# Use list comprehension in your solution.
#
# EXAMPLES
# destroy_elements([1, 2, 3], [1, 2])      => [3]
# destroy_elements([1, 2, 3], [1, 2, 3])   => []
# destroy_elements([1, 2, 3], [4, 5])      => [1, 2, 3]