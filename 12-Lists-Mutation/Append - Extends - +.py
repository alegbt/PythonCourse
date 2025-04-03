##APPEND - modifica l'existing list aggiungendo 1 valore

countries = ["italy", "france"]
countries.append("usa")
print(countries) ##['italy', 'france', 'usa']
countries.append(["ugo", "pino"])
print(countries) ##['italy', 'france', 'usa', ['ugo', 'pino']]

##EXTENDS - fa 1 append di 1 lista ad 1 altra lista

countries.extend(["abc", "def"])
print(countries) ##['italy', 'france', 'usa', ['ugo', 'pino'], 'abc', 'def']

## + operator - crea 1 nuova list
newList = ["new1", "new2"]
thirdList = newList + countries
print(thirdList) ##['new1', 'new2', 'italy', 'france', 'usa', ['ugo', 'pino'], 'abc', 'def']