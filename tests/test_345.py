from leetcode.easy.m_345 import reverse_vowels

def test_reverse_vowels_case_1():
        
    s = "hello"
    
    expected = "holle"
    result = reverse_vowels(s)
    
    assert expected == result

def test_reverse_vowels_case_2():
        
    s = "leetcode"
    
    expected = "leotcede"
    result = reverse_vowels(s)

    assert expected == result

