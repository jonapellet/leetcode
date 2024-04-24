from leetcode.medium.m_151 import reverse_words


def test_reverse_words_case_1():
    assert reverse_words("the sky is blue") == "blue is sky the"

def test_reverse_words_case_2():
    assert reverse_words("  hello world  ") == "world hello"

def test_reverse_words_case_3():
    assert reverse_words("a good   example") == "example good a"