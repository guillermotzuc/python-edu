# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
class RotateArray:

    def rotate2(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        array_length = len(nums) - 1
        for i in range(target):
            array = [array[array_length]] + array
            array.pop()
        nums[:] = array
        print(nums)

    def rotate(self, array, target):
        """

        Args:
            array (_type_): _description_

        >>> rotate_array = RotateArray()
        >>> array = [1,2,3,4,5,6,7]
        >>> target = 3
        >>> rotate_array.rotate(array, target)
        [5, 6, 7, 1, 2, 3, 4]

        >>> rotate_array = RotateArray()
        >>> array = [-1,-100,3,99]
        >>> target = 2
        >>> rotate_array.rotate(array, target)
        [3, 99, -1, -100]
        """
        array_length = len(array) - 1
        for i in range(target):
            array = [array[array_length]] + array
            array.pop()

        return array

if __name__ == "__main__":
    rotate_array = RotateArray()
    array = [1,2,3,4,5,6,7]
    target = 3
    print(rotate_array.rotate2(array, target))