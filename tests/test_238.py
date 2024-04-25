from leetcode.medium.m_238 import product_except_self

def test_product_except_self_case_1():
    
    nums = [1,2,3,4]
    
    expected = [24,12,8,6]
    result = product_except_self(nums)
    
    assert expected == result

def test_product_except_self_case_2():
    
    nums = [-1,1,0,-3,3]
    
    expected = [0,0,9,0,0]
    result = product_except_self(nums)
    
    assert expected == result
