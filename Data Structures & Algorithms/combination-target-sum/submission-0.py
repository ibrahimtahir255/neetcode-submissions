class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        def backtrack(index, current):
            # base case
            if index == len(nums):
                return
            if sum(current) == target:
                result.append(current)
                return
            else:
                if sum(current) > target:
                    return

            # at each step
            # include
            backtrack(index, current + [nums[index]])

            # exclude
            backtrack(index + 1, current)
        
        backtrack(0, [])
        
        return result



        