# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# 
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
# 
# Example 1:
# 
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# 
# Example 2:
# 
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# 
# Example 3:
# 
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
# 
#  
# 
# Constraints:
# 
#     1 <= str1.length, str2.length <= 1000
#     str1 and str2 consist of English uppercase letters.

def gcd(a: str, b:str) -> str:

    # abcabc, abcxx -> ''
    # abcxx, abc -> ''

    # produce the factors of s1
    # produce the factors of s2
    # calculate their intersection (factors of both s1 and s2)
    # take the max of the intersection

    def find_factors(S):
        factors = set([S])
        for i in range(1, len(S) // 2 + 1):
            if len(S) % i == 0:
                t = S[:i]
                if t * (len(S) // i) == S:
                    factors.add(t)
        return factors

    factors1 = find_factors(a)
    factors2 = find_factors(b)

    common_factors = factors1.intersection(factors2)

    # find the max of the common factors
    if len(common_factors) > 0:
        return max(common_factors, key=len)
    else:
        return ''