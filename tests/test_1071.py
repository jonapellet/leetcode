from leetcode.easy.m_1071 import gcd

def test_gcd_case_1a():
    
    str1 = "ABCABC"
    str2 = "ABC"

    expected = "ABC"
    result = gcd(str1, str2)

    assert expected == result

def test_gcd_case_1b():
    """ Result must not depend on the ordering of the strings """
    
    str1 = "ABCABC"
    str2 = "ABC"

    expected = "ABC"
    result = gcd(str2, str1)

    assert expected == result

def test_gcd_case_2():
    
    str1 = "ABABAB"
    str2 = "ABC"

    expected = "AB"
    result = gcd(str1, str2)

    assert expected == result

def test_gcd_case_2():
    
    str1 = "LEET"
    str2 = "CODE"

    expected = ""
    result = gcd(str1, str2)

    assert expected == result