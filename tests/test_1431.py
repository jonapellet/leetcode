from leetcode.easy.m_1431 import kids_with_candies

def test_kids_with_candies_case_1():
    
    candies = [2,3,5,1,3]
    extra_candies = 3
    
    expected = [True, True, True, False, True]
    result = kids_with_candies(candies, extra_candies)
    
    assert expected == result

def test_kids_with_candies_case_2():
    
    candies = [4,2,1,1,2]
    extra_candies = 1
    
    expected = [True, False, False, False, False]
    result = kids_with_candies(candies, extra_candies)
    
    assert expected == result

def test_kids_with_candies_case_3():
    
    candies = [12,1,12]
    extra_candies = 10
    
    expected = [True, False, True]
    result = kids_with_candies(candies, extra_candies)
    
    assert expected == result