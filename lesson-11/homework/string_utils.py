def reverse_string(s):
    return s[::-1]


def count_vowels(s):
    vowels = 'aeiou'
    k = 0

    for i in s:
        if i.lower() in vowels:
            k += 1
    return k


    