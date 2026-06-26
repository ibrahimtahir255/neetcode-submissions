class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        U:
        Can we have negative numbers?
        Can we have a zero?
        Edge Cases:
        if nums = [] return []
        if nums just ahs two difits then return as is

        M:
        Data Structure: Two arrays (prefix and suffix)
        Pattern: Prefix and suffix products
        """

    
        
        # initialize both arrays
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        out_list = [1] * len(nums)
        # run a loop left to write
        for i in range (1, len(nums)):
            # build prefix
            prefix[i] = prefix[i-1] * nums[i-1]
        # run a loop right to left
        for i in range (len(nums)-2, -1, -1):
            # build suffix
            suffix[i] = suffix[i+1] * nums[i+1]
        
        # loop and multiple pprefix and suffix
        for i in range (len(nums)):
            out_list[i] = prefix[i] * suffix[i]

        return out_list

        