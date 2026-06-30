class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        U:

        Can there by duplicates? Every number appears once?
        What if input is empty list

        edge cases:
        if nums = [], target = ; return []

        M: 
        Data structure: List
        pattern: two pointers, opposite ends, move based on sum comparison
        """

        
        # inialize the pointers
        left = 0
        right = len(numbers) - 1

        # while loop until left and right pointer meet/ are equal
        while left < right:
            sum = numbers[left] + numbers[right]
            # if (sum of pointers) is greater than target
            if sum > target:
                # dec right
                right -= 1
            # elif (sum of pointers) is lesser than target
            elif sum < target:
                # inc left
                left += 1
            # else return the indices
            else:
                return [left + 1, right + 1]
        
        