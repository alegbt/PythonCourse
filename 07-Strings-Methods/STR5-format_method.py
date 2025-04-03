


# .format()

mad_libs = "{} laughed at the {} {}."
print(mad_libs.format("ale", "red", "alien")) # ale laughed at the red alien.
print(mad_libs.format(1, 2, 3)) # 1 laughed at the 2 3.
print(mad_libs.format(1, 2, 3, 4, 5, 6, 7)) # 1 laughed at the 2 3.  - non succede niente con + params, se ce ne fossermo meno darebbe errore

mad_libs2 = "{1} laughed at the {0} {2}"
print(mad_libs2.format("ale", "red", "alien")) # red laughed at the ale alien
print(mad_libs2.format(1, 2, 3)) # 2 laughed at the 1 3

mad_libs3 = "{name} laughed at the {adjective} {noun}"
print(mad_libs3.format(name="ale", adjective="red", noun="alien")) # ale laughed at the red alien
print(mad_libs3.format(noun=1, adjective=2, name=3)) # 3 laughed at the 2 1



name = input("enter name: ")
adjective = input("enter adjective: ")
noun = input("enter noun: ")

print(mad_libs3.format(name=name, adjective=adjective, noun=noun))
