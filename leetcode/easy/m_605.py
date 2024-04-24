# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# 
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
# 
# 
# Example 1:
# 
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# 
# Example 2:
# 
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
# 
#  
# 
# Constraints:
# 
#     1 <= flowerbed.length <= 2 * 104
#     flowerbed[i] is 0 or 1.
#     There are no two adjacent flowers in flowerbed.
#     0 <= n <= flowerbed.length
#  
from typing import List

def can_place_flowers(flowers_bed: List[int], n:int) -> bool:
    # great for the theoritical mind, without regard to the efficiency of the code lol.

    def index_of_flower(flowers):
        # for all position in the flowerbed. check what is left and right of the position
        for i in range(len(flowers)):
            left = flowers[i - 1] if i > 0 else 0 # we assume we can place a flower at the beginning of the flowerbed
            right = flowers[i + 1] if i < len(flowers) - 1 else 0 # we assume we can place a flower at the end of the flowerbed
            free = flowers[i] == 0

            if left == 0 and right == 0 and free:
                return i

        return None

    if n == 0:
        return True
    elif n == 1:
        flower_location = index_of_flower(flowers_bed)
        if flower_location is not None:
            return True
        else:
            return False
    else:
        flower_location = index_of_flower(flowers_bed)
        if flower_location is not None:
            flowers_bed[flower_location] = 1
            return can_place_flowers(flowers_bed, n - 1)
        else:
            return False

