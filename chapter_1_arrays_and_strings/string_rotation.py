def is_substring(string, sub):
    return string.find(sub) != -1


def is_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return is_substring(s1+s1, s2)
    else:
        return False


print(is_rotation('waterbottle', 'erbottlewat'))
print(is_rotation('foo', 'bar'))
print(is_rotation('foo', 'foofoo'))