class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        U:
        edge cases:
        if nums == [] then return what?

        M:
        Data structure: Hashmap
        Pattern: num --> index

        """

        
        # intialize a dict
        my_dict = {}
        # loop through the list
        for i in range (len(nums)):
            target_num = target - nums[i]
            if target_num in my_dict:
                return [my_dict[target_num], i]
            # add it and initialize it with i
            my_dict[nums[i]] = i 
        return []

        