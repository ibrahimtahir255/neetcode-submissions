class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums = sorted(nums)

        def backtrack(index, current):
            print(f"index={index}, current={current}")
            if index == len(nums):
                results.append(current)
                return

            
            # at each step
            # include 
            backtrack(index+1, current+[nums[index]])

            # exclude 
            # but first skip all duplicates
            next_index = index +1
            while next_index < len(nums) and nums[next_index] == nums[index]:
                next_index += 1
            
            backtrack(next_index, current)

        backtrack(0, [])

        return results