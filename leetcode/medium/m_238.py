# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
#  
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#
# Example 2:
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#  
#
# Constraints:
#
#     2 <= nums.length <= 105
#     -30 <= nums[i] <= 30
#     The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# NOTE: This currently fails the leetcode submission....

from typing import List
from functools import reduce
import operator

def product_except_self(nums: List[int]) -> int:

    # consider the numbers of 0 in the list carefully
    def count_zeros(a,b):
        if b == 0:
            return a + 1
        return a

    num_zeros = reduce(count_zeros, nums, 0)

    if num_zeros > 1:
        return [0] * len(nums)

    elif num_zeros == 1:
        # find the index of the zero
        zero_index = nums.index(0)

        # replace it by 1
        nums[zero_index] = 1

        # compute the product of all items
        product = reduce(operator.mul, nums)

        # produce a list of zeros
        result = [0] * len(nums)

        # replace the zero index by the product
        result[zero_index] = product

        return result

    else:

        product = reduce(operator.mul, nums)

        def my_division(numerator, denominator):
            # sometimes, you got to make your own division function
            sign_numerator = 1 if numerator > 0 else -1
            sign_denominator = 1 if denominator > 0 else -1

            numerator = abs(numerator)
            denominator = abs(denominator)

            result = 0
            while numerator > 0:
                numerator -= denominator
                result += 1

            return result * sign_numerator * sign_denominator

        return [my_division(product, num) for num in nums]






        