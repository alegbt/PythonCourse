##printing each char from a string

dinner = "steak and potatoes"

for c in dinner:
    print(c)

listFood = ["potatoes", "steak", "ribs"]

for l in listFood:
    print(len(l))

print(l)



##iterate in reverse
##genrates a new list


the_simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]

for character in the_simpsons[::-1]:
    print(f"{character} has a total of {len(character)} characters.")

##reversed gives back a generator object not a list
for character in reversed(the_simpsons):
    print(f"{character} has a total of {len(character)} characters.")



###ENUMERATE function
##returns a generator object
##e' un for che tiene l'index e la value ogni loop

errands = ["Go to gym", "Grab lunch", "Get promoted at work", "Sleep"]

for index, element in enumerate(errands, 0):
    print(f"{element} is number {index} on my list of things to do today!")



##range function
##crea un Range object che ha tutti i numeri da N a M
##Range e' iterabile
##The function range(start, stop, step) generates numbers from start to stop - 1, increasing by step.

for n in range(5):
    print(n) ##0 1 2 3 4


for n in range(2, 5):
    print(n) ##2 3 4

for n in range(2, 10, 3):
    print(n) ##2 5 8

for n in range(99, -1, -11):
    print(n) ##99 88 77 66 55 44 33 22 11 0



##BREAK keyword
##stops for loop and exits








