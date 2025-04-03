# Write a factors function that accepts a positive whole number
# It should return a list of all the number's factors in ascending order
# HINT: Could the range function be helpful here? Or maybe a while loop?
#
# EXAMPLES
# factors(1)  => [1]
# factors(2)  => [1, 2]
# factors(10) => [1, 2, 5, 10]
# factors(64) => [1, 2, 4, 8, 16, 32, 64]

def factors(n1):
    nums = []
    for n in range(1, n1+1):
        if n1%n == 0:
            nums.append(n)

factors(2)


# Declare a delete_all function that accepts a list of strings and a target string
# Remove all occurrences of the target string from the list and return it
#
# EXAMPLES
# delete_all([1, 3, 5], 3)  => [1, 5]
# delete_all([5, 3, 5], 5)  => [3]
# delete_all([4, 4, 4], 4)  => []
# delete_all([4, 4, 4], 6)  => [4, 4, 4]


def delete_all(items, target):
    while target in items:
        items.remove(target)
    print(items)
    return items

delete_all([1,2,2,3], 2)


def push_or_pop(items):
    newVals = []
    for val in items:
        if val > 5:
            newVals.append(val)
        elif newVals:
            newVals.pop(-1)
    print(newVals)

push_or_pop([10, 20, 30])
push_or_pop([10, 20, 2 , 30])