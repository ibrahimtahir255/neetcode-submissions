class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(index, current):
            if index == len(nums):
                result.append(current)
                return
            
            # include
            backtrack(index+1, current + [nums[index]])
            
            # exclude 
            backtrack(index+1, current)

        backtrack(0, [])

        return result

        