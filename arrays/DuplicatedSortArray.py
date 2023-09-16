#!/usr/bin/env python3.7

# Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates 
# in-place such that each unique element appears only once. The relative order of the 
# elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need 
# to do the following things:

# Change the array nums such that the first k elements of nums contain the unique 
# elements in the order they were present in nums initially. The remaining elements of 
#  nums are not important as well as the size of nums.
# Return k.
 

#def remove_duplicated_from_array(array):
#    array_pos = 0
#    for index, item in enumerate(array):
#        if item > array[array_pos]:
#            array_pos = array_pos + 1
#            array[array_pos] = item
#            array[index] = "_"
#        elif index != 0 and index != array_pos:
#            array[index] = "_"
#    return array_pos

class Solution:
    def removeDuplicates(nums) -> int:
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
                # Found unique element
            if nums[i - 1] != nums[i]:      
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i] 
                # Incrementing insertIndex count by 1 
                insertIndex = insertIndex + 1       
        
        return insertIndex

    #print(remove_duplicated_from_array([0,0,1,1,1,2,2,3,3,4]))
    nums = [1,1,2]
    print(removeDuplicates(nums))