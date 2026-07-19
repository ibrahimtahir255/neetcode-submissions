class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        U: 
        Edge case: [] return False
        M:
        Data Structure: Set
        Pattern: Tracking seen elements

        """

        
        # intialize an empty set
        my_set = set()

        # loop through each num in nums
        for num in nums:
            # if num is already in the set
            if num in my_set:
                # return True immediately
                return True
            # add num to set
            my_set.add(num)
        return False



        