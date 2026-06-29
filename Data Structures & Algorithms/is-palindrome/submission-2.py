class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        U: 
        is it case insenstive
        is it onyl alpha numberic characters? 

        Edge cases:
        if s= "" return true
        """

        # convert everything to lowercase
        lower_str = s.lower()
        # intialize left, right pointers
        left = 0 
        right = len(lower_str) - 1

        # loop through the string until left=right
        while left < right and left != right:
            # check if item is non alphanumeric
            if left < right and not (lower_str[left].isalnum()): 
                left = left + 1
            elif right > left and not (lower_str[right].isalnum()):
                right = right - 1
            else:
                # check if left pointer and right pointer have diff values
                if lower_str[left] != lower_str[right]:
                    return False
                left = left + 1
                right = right - 1
        
        return True
        