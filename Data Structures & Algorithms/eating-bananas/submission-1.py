class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Does k have to be a whole number or can it also be a fraction?
        We could divide the time equally between piles but some piles have more
        bananas to eat so how do we give weightage to that?

        

        """

        # if k works try smaller, if k doesnt work try larger
        low = 1
        high = max(piles)
        min_k = float('inf')

        # bianry search
        while low <= high:
            k = (low + high) // 2
            sum_hr = 0

            for index in range (len(piles)):
                # sum the num of hours taken
                sum_hr += math.ceil(piles[index]/k)
            
            if sum_hr <= h:
                if k < min_k:
                    min_k = k                
                high = k - 1
            else:
                low = k + 1
        return min_k
        
                     
