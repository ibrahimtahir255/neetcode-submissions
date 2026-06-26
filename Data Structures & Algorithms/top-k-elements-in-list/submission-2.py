class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        U:
        Can return the output in any order? 
        What if the elements that are the most frequent are greater than k. What do we pick then?
        Edge cases:
        if nums = [] --> []
        if k = 0 --> []
        """

        
        
        # initialize a hashmap
        my_dict = {}
        # loop through the list
        for num in nums:
            # check if num in dict
            if num in my_dict:
                # increase frequency
                my_dict[num] += 1
            # else add num to dict and assign frequnecy to 1
            else:
                my_dict[num] = 1

        # sort the dict in descending order and choose top k keys
        sorted_dict = sorted(my_dict, key= lambda x: my_dict[x], reverse=True)

        # return them as a list 
        return sorted_dict[:k]