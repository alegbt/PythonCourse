count = 0

while count <= 5:
    print(count)
    count += 1

# questo non pritna perche count e' gia a 5
while count <= 5:
    print(count)
    count += 1

invalid_num = True

while invalid_num:
    value = int(input("put a num above 10\n"))
    if value > 10:
        invalid_num = False
