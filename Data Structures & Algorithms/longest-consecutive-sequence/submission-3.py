class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        U:
        What do we do with deuplicates? -> ignore them
        Edge cases:
        if nums=[] return 0

        M:
        Data Structure: Set
        Pattern: add to list
        """

        
        # intilaize a set
        my_set = set(nums)

        # Initialize max length
        max_len = 0

        # loop through the set
        for item in my_set:
            # if prev does exist (means current is the start) then start the 
            if (item - 1) not in my_set:
                # inialize current length
                current_length = 1
                while (item + 1) in my_set:
                    # increment current_num
                    item = item + 1
                    # increment the length variable
                    current_length += 1
            
                # compare to max length
                max_len = max(max_len, current_length)
        return max_len
        
        