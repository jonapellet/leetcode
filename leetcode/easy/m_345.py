from functools import reduce

def reverse_vowels(s: str) -> str:

    vowels = set('aeiouAEIOU')
    s_vowels = ''

    for c in s:
        if c in vowels:
            s_vowels += c

    # reverse the vowels
    s_reversed_vowels = list(s_vowels[::-1])

    # make a list out of the initial string
    s_list = list(s)

    next_vowel_idx = 0

    # modify in place the vowels
    for i,c in enumerate(s_list):
        if c in s_vowels:
            s_list[i] = s_reversed_vowels[next_vowel_idx]
            next_vowel_idx += 1

    return "".join(s_list)

