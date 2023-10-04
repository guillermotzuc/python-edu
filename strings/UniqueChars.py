
class UniqueChars:
    """Validate if any char is more than once
    """
    
    def unique_chars(sefl, string_value):
        """
        Validate if any char is more than once

        Args:
            string_value (str): _description_

        Returns:
            Boolean : _description_
        
        >>> string_value = 'pepito'
        >>> uniqueChars = UniqueChars()
        >>> uniqueChars.unique_chars(string_value)
        True

        >>> string_value = 'abc'
        >>> uniqueChars = UniqueChars()
        >>> uniqueChars.unique_chars(string_value)
        False
        """
        for i in range(len(string_value)):
            if string_value.count(string_value[i]) > 1:
                return True
        return False


if __name__ == "__main__":
    uniqueChars = UniqueChars()
    string_value = "abc"
    print(uniqueChars.unique_chars(string_value))