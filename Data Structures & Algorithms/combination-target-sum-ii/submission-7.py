class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)
        
        def backtrack(index, current):
            # base cases
            if sum(current) == target:
                result.append(current)
                return
            if index == len(candidates):
                return
            if sum(current) > target:
                return
            

            # at each step
            # include
            backtrack(index+1, current + [candidates[index]])

            # exclude
            next_index = index + 1
            while next_index < len(candidates) and candidates[index] == candidates[next_index]:
                next_index += 1
            backtrack(next_index, current)

        backtrack(0, [])
        return result
