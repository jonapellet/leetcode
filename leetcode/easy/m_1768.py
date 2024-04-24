# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
#
# Return the merged string.
#
#  
#
# Example 1:
#
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
#
# Example 2:
#
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
#
# Example 3:
#
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
#
#  
#
# Constraints:
#
#     1 <= word1.length, word2.length <= 100
#     word1 and word2 consist of lowercase English letters.

def merge_alternate(word1: str, word2) -> str:

    # 'abc', 'xyzw' -> 'axbyczw'

    def alt_gen(word1, word2):
        # take the len of word1 and word2 by taking len of word1
        remaining_w1 = len(word1)
        remaining_w2 = len(word2)

        while remaining_w1 > 0 or remaining_w2 > 0:
            if remaining_w1 > 0:
                yield word1[len(word1) - remaining_w1]
                remaining_w1 -= 1
            if remaining_w2 > 0:
                yield word2[len(word2) - remaining_w2]
                remaining_w2 -= 1

        return 

    return ''.join(alt_gen(word1, word2))

