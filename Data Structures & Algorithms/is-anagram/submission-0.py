class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
        U:
        edge case:
            if s = "" and t = "" return True
            if len(s) != len(t) return False
        
        M:
        Data structure: hash map
        Pattern: track the frequency of characters
        
        """

        
        # P:
        # if len(s) != len(t) return False
        if len(s) != len(t):
            return False

        # intialize a haspmap/dict
        my_dict = {}

        # loop through len(s)
        for i in range (len(s)):
            # if char is not already in hashmap
            if s[i] not in my_dict:
                # add it and intialize to 0
                my_dict[s[i]] = 0
            # add 1 to the frequency of s
            my_dict[s[i]] += 1
            
            # do the same checks for t 
            if t[i] not in my_dict:
                my_dict[t[i]] = 0
            # remove 1 from the frequency of d
            my_dict[t[i]] -= 1

        # loop through dict:
        for key in my_dict:
            # if value in dict != 0
            if my_dict[key] != 0:
                return False
        return True

        