

# lstrip() e rstrip()  e strip- lstrip e rstrip rimuoveonogli spazi a sx o dx , strip rimuove tutti gli spazi

empty_space = "   words     "

print(empty_space.strip()) #words
print(empty_space.rstrip()) #    words
print(empty_space.lstrip()) #words      #
# con param puoi rimuovere dei pattern all'inizio o fine di una str
website = "www.python.orgw"
print(website.lstrip("w")) # .python.orgw
print(website.rstrip(".orgw")) # www.python
print(website.strip("w")) # .python.org  - fa strip ad inizio e fine


# .replace()
phone = "555 123 1324"
print(phone.replace(" ", "-")) # 555-123-1324
print(phone.replace("5", "X")) # 555-123-1324

