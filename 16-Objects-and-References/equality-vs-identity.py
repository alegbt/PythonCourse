import copy

nums = [1,2,3]
a = [0, nums, 4]

#sono tuti metodi che fanno la stessa cosa cioe la shallow copy
b = a[:]
b = a.copy()
b = copy.copy(a)

#la shallow copy copia l'elemento ma anche le reference dei valori primitivi immutabili ( gli integer lo sono)
# quindi va a prendere la reference i nmemoria dei valori interni , infatti a[1] is b[1]
print(a==b) #true
print(a is b) #false
print(a[1] is b[1]) #true
a[1].append(100)
#modificandone uno si modifica anche il secondo
print(a) #[0, [1, 2, 3, 100], 4]
print(b) #[0, [1, 2, 3, 100], 4]

#la deepcopy crea nuovi valori in memoria per creare l'altra value infatti a[1] not is b[1]
b = copy.deepcopy(a)
print(a==b) #t
print(a is b) #f
print(a[1] is b[1]) #f
a[1].append(100)
#modificandone uno NON si modifica anche il secondo
print(a) #[0, [1, 2, 3, 100, 100], 4]
print(b) #[0, [1, 2, 3, 100], 4]