class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        U:
        Can there be duplicates?
        Is this case senstitive?

        edge cases:
        if str = "" -> 0
        if all same char in the string -> 1

        M:
        hashmap for storing and updating indices.
        two pointer
        """
        
    
        
        # initialize pointer
        left = 0
        
        # intialize dict
        my_dict = {}

        # intialize longest
        longest = 0

        for right in range (len(s)):
            # check for duplicate
            if s[right] in my_dict and my_dict[s[right]] >= left:
                left = my_dict[s[right]] + 1

            # update hashmap
            my_dict[s[right]] = right

            # update longest
            longest = max(longest, right-left +1)
        return longest