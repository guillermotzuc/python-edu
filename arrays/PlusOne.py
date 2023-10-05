
class PlusOne:
    """
    You are given a large integer represented as an integer array digits, where each digits[i] is 
    the ith digit of the integer. The digits are ordered from most significant to least significant 
    in left-to-right order. The large integer does not contain any leading 0's.
    
    Increment the large integer by one and return the resulting array of digits.

    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
    Incrementing by one gives 123 + 1 = 124.
    Thus, the result should be [1,2,4].

    Input: digits = [9]
    Output: [1,0]
    Explanation: The array represents the integer 9.
    Incrementing by one gives 9 + 1 = 10.
    Thus, the result should be [1,0].

    >>> array = [9,9,9]
    >>> plusOne = PlusOne()
    >>> plusOne.get_plus_one(array)
    [1, 0, 0, 0]

    >>> array = [9,8,9]
    >>> plusOne = PlusOne()
    >>> plusOne.get_plus_one(array)
    [9, 9, 0]

    """

    def get_plus_one(self, array):
        """ Get the plus one from the given array

        Args:
            array (numbers): represents the number array
        """
        length_array = len(array) -1
        for number in array[::-1]:
            if number < 9:
                array[length_array] += 1
                return array
            else:
                array[length_array] = 0
            length_array -= 1

        if array[0] == 0:
            return [1] + array

        return array

if __name__ == "__main__":
    plusOne = PlusOne()
    array = [9,9,9]
    print(plusOne.get_plus_one(array))