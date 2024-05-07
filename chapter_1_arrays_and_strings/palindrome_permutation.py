from collections import defaultdict


def palindrome_permutation(string):
    string_dict = defaultdict(int)
    word_len = 0
    for char in string:
        if char.isalpha():
            if string_dict[char]:
                string_dict[char] -= 1
                if string_dict[char] == 0:
                    del string_dict[char]
            else:
                string_dict[char] += 1
        else:
            word_len -= 1

    length = len(string) - word_len
    if length % 2 == 0 and len(string_dict) == 0:
        return True

    elif length % 2 != 0 and len(string_dict) == 1:
        for k, v in string_dict.items():
            if v == 1:
                return True
    else:
        return False


print(palindrome_permutation("tact cao"))
print(palindrome_permutation('tactc oapapa'))
print(palindrome_permutation('azAZ')) # wrong answer