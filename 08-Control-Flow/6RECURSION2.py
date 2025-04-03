
def reverse(strq):
    rev_index = len(strq) -1
    rev_str = ""
    while rev_index >= 0:
        rev_str += strq[rev_index]
        rev_index -= 1
    print(rev_str)


reverse("ciao")


def reverse_recursive(strq):
    if len(strq) <= 1:
        return strq
    return strq[-1] + reverse_recursive(strq[:-1])


print(reverse_recursive("ciao"))
