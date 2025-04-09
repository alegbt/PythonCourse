
##GET
## restituisce la key

dictionary1 = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}

print(dictionary1.get("key1")) #value1
print(dictionary1.get("key4", "value5")) # ritorna la 2 value se non esiste la 1
print(dictionary1) #dictionary non e' stato cambiato


## SETDEFAULT
## aggiugne una key pair
## edita solo se la key non e' assegnata
dictionary1.setdefault("key4", "value4") #aggiunge key4 dato che key4 non esiste nel dictionary
dictionary1.setdefault("key3", "value4") #non fa nulla perche key3 e' gia assegnata
print(dictionary1) #{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}



## POP
## rimuove 1 key - value e la ritorna

values = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}

values2 = values.pop("key1")
print(values2) #value1
#values2 = values.pop("key4") #error se non esiste la key
values2 = values.pop("key4", None) #restituisce l'alternativa se non esiste la prima key
print(values2) #secondaryValue
print(values) # {'key2': 'value2', 'key3': 'value3'} e' stata tolta key1


# DEL
# rimuove 1 key - value senza ritornare nulla
# errore se non trova la key
del values["key2"]
print(values) # {'key3': 'value3'}



#CLEAR
# clear del dictionary

values2 = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}

values2.clear()
print(values2)


# UPDATE
# merges 1 dictionary into another
# edits the dictionary that's calling te method leaving unscathed the other

values = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}

values2 = {
    "key1": "aaa",
    "key2": "bbb",
    "key6": "ccc",
}

values.update(values2)
print(values) #{'key1': 'aaa', 'key2': 'bbb', 'key3': 'value3', 'key6': 'ccc'}



##DICT function
## converts a list (if possible) to adictionary

##dict funziona xke sintassi compatibile per la conversione
elems  = [
    ["elem1", "value1",],
    ["elem2", "value2"],
    ["elem3", "value3",]
]

print(dict(elems)) ##{'elem1': 'value1', 'elem2': 'value2', 'elem3': 'value3'}


#NESTED DICTIONARIES
tv_shows = {
    "The X-Files": {
        "Season 1": {
            "Episodes": ["Scary Monster", "Scary Alien"],
            "Genre": "Science Fiction",
            "Year": 1993
        },
        "Season 2": {
            "Episodes": ["Scary Conspiracy"],
            "Genre": "Horror",
            "Year": 1994
        }
    },
    "Lost": {
        "Season 1": {
            "Episodes": ["What The Heck Is Happening On This Island?"],
            "Genre": "Science Fiction",
            "Year": 2004
        }
    }
}

print(tv_shows["The X-Files"]["Season 1"]["Episodes"][1])
print(tv_shows["Lost"]["Season 1"]["Year"])