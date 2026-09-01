class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        visited = [False]*len(nums)
        def backtrack(current):
            # base case 
            if len(nums) == len(current):
                results.append(current[:])
                return
            
            # at each step
            for i in range (len(nums)):
                # if nums[i] has not been visited then pick it
                if not visited[i]:
                    visited[i] = True
                    current.append(nums[i])
                    backtrack(current)
                    visited[i] = False
                    current.pop()
        backtrack([])

        return results
        



        
        