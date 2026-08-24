class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        existing_subset = [[]]
        new_subset = []
        
        for i in range (len(nums)):
            to_add = []
            for subset in existing_subset:
                new_subset = subset + [nums[i]]
                to_add.append(new_subset)
            existing_subset.extend(to_add)

        # print("subsets: ", new_subset)
        return existing_subset