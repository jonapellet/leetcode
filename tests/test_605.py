from leetcode.easy.m_605 import can_place_flowers


def test_can_place_flowers_case_1():
    
    flowers_bed = [1,0,0,0,1]
    n = 1
    
    expected = True
    result = can_place_flowers(flowers_bed, n)
    
    assert expected == result


def test_can_place_flowers_case_2():
    
    flowers_bed = [1,0,0,0,1]
    n = 2
    
    expected = False
    result = can_place_flowers(flowers_bed, n)
    
    assert expected == result