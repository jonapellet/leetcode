from leetcode.easy.m_1768 import merge_alternate


def test_merge_altertate_case_1():
    
    word1 = "abc"
    word2 = "pqr"

    expected = "apbqcr"
    result = merge_alternate(word1, word2)

    assert expected == result


def test_merge_altertate_case_2():
    
    word1 = "ab"
    word2 = "pqrs"

    expected = "apbqrs"
    result = merge_alternate(word1, word2)

    assert expected == result

def test_merge_altertate_case_3():
    
    word1 = "abcd"
    word2 = "pq"

    expected = "apbqcd"
    result = merge_alternate(word1, word2)

    assert expected == result