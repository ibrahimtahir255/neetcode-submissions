class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        U:
        Can we assume the dostance between each height is 1 unit?

        edge cases:
        if heights = [] then return 0
        if len(heights) == 1 then return 0

        M:
        - two pointer
        - area = min(heights[left], heights[right]) * (right - left)

        """

        
        # intialize the pointers
        left = 0
        right = len(heights) - 1

        # intialize max area variable
        max_area = 0

        # while loop around heights
        while left < right:
            # calculate the area
            area = min(heights[left], heights[right]) * (right - left)
            
            if area > max_area:
                max_area = area

            if heights[left] > heights[right]:
                # dec right
                right -= 1
            elif heights[left] < heights[right]:
                # inc left
                left += 1
            # else what if they are equal?? do whatever inc left?
            else:
                left += 1
        return max_area
        