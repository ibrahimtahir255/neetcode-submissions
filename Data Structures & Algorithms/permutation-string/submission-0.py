class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        U:

        Are characters just alphabets?
        are they all lowercase?

        edge case:
        if s1 = "", s2= "" -> true

        """

        
        # initialize left pointer
        left = 0

        # inialize two dicts one for s1 and one for the window
        dict_s1 = {}
        dict_s2 = {}

        # build s1 hashmap before the loop
        for char in s1:
            if char not in dict_s1:
                dict_s1[char] = 1
            else:
                dict_s1[char] += 1
        
        # main window loop
        for right in range (len(s2)):
            # initialize or update s2 hashmap
            if s2[right] not in dict_s2:
                dict_s2[s2[right]] = 1
            else:
                dict_s2[s2[right]] += 1

            window_size = right - left + 1

            # if window too big -> shrink 
            if window_size > len(s1):
                # decrement frequency of element at left in hashmap of window
                dict_s2[s2[left]] -= 1
                if dict_s2[s2[left]] == 0:
                    del dict_s2[s2[left]] 
                # move left
                left += 1
            # if dicts equal return true
            if dict_s1 == dict_s2:
                return True
        return False
        
                
        