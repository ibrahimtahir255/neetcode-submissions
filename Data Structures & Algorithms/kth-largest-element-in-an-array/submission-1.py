class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # initialize heap
        self.heap = []
        # populate heap by engating because we need max heap
        for num in nums:
            heapq.heappush(self.heap, -num)

        # while k
        while k:
            k -= 1
            # keep popping - negate
            kth_largest = -heapq.heappop(self.heap)

        # return the last element popped
        return kth_largest
        