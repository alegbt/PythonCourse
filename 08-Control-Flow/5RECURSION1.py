def count_down(n):
    start = n
    while start > 0:
        print(start)
        start -= 1


# count_down(5)


def count_down_recursive1(n):
    if n > 0:
        print(n)
        count_down_recursive(n - 1)


def count_down_recursive(n):
    if n <= 0:
        return
    print(n)
    count_down(n - 1)


count_down_recursive(5)
count_down_recursive1(5)
