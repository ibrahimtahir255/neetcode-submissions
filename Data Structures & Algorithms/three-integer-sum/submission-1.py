class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """
        U:
        Can their be dupilicates int eh input?
        Can the solution have duplicates?
        Cant he input be []

        Edge case:
        if nums = [] return []

        M:
        Data structure:
        Pattern: 
        """
    
        # sort the list in ascending order
        nums_sorted = sorted(nums)

        out_list = []

        # outer for loop for fixed points
        for i in range (len(nums_sorted)):
            # if not visited
            if i>0 and nums_sorted[i] == nums_sorted[i-1]: 
                continue

            # initialize the pointers
            left = i + 1
            right = len(nums_sorted) - 1

            # while loop until left and right pointer meet/ are equal
            while left < right and left != right:
                sum = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]
                # if (sum of pointers) is greater than target
                if sum > 0:
                    # dec right
                    right -= 1
                # elif (sum of pointers) is lesser than target
                elif sum < 0:
                    # inc left
                    left += 1
                # else append to output list
                else:
                    # append to output list 
                    out_list.append([nums_sorted[i],nums_sorted[left],nums_sorted[right]])
                    # skip duplicates of left 
                    while left < right and nums_sorted[left] == nums_sorted[left+1]:
                        left += 1
                    # ski pduplicates on right 
                    while left < right and nums_sorted[right] == nums_sorted[right -1]:
                        right -= 1
                    # move the pointers inwards if not duplicates
                    left += 1
                    right -= 1

        return out_list

