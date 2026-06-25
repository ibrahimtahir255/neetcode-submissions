class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        U: 
        Edge cases:
        if List = [] return [[""]]
        if only one item return [["item"]

        M:
        Data Structure: hashmap
        Pattern: sorted word as key to group anagrams

        """

    
        # initialize a hashmap
        my_dict = {}

        # loop through the length of the input list
        for item in strs:
            # check if item.sort in dict
            sorted_item = ''.join(sorted(item))
            if sorted_item in my_dict:
                # add item to the appropriate key
                my_dict[sorted_item].append(item)
            # if not in dict create a new key for item.sort
            else:
                my_dict[sorted_item] = [item]
        
        # return the final list
        return list(my_dict.values())

        