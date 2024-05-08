import collections


def str_compression(string):
    char_counts = collections.Counter(string)
    result = []
    for k, v in char_counts.items():
        result.append(str(k))
        result.append(str(v))
    comp_str = ''.join(result)
    if len(result) < len(string):
        return comp_str
    return string

print(str_compression('abcdef'))
