#!/usr/bin/env python3.7

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order
# Example 1: 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# x + y = 9 where x and y in [2,7,11,15]
# x = 9 - y
# y = 9 - x

class TwoSum:

    def getTwoSumArray(self, array, target):
        """
        Get two elements in the array that sum {target}

        Args:
            array (array): y values array 
            target (number): target number
        
        >>> twoSum = TwoSum()
        >>> target = 9
        >>> array = [2,7,11,15]
        >>> twoSum.getTwoSumArray(array, target)
        [7, 2]
        """
        dictionary = {}
        for item in array:
            y = target - item
            if y in dictionary:
                return [item, y]
            else:
                dictionary[item] = y
        
        return []

if __name__ == "__main__":
    twoSum = TwoSum()
    target = 9
    array = [2,7,11,15]
    print(twoSum.getTwoSumArray(array, target))
    