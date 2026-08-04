class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # initialize a heap
        self.heap = []
        # create heap
        for stone in stones:
            heapq.heappush(self.heap, -stone)

        # keep simualting until there is no more than one stone remaining
        while len(self.heap) > 1:
            x = -heapq.heappop(self.heap)
            y = -heapq.heappop(self.heap)
            # if x>y
            if x > y:
                # calcualte the new weight
                new_weight = x-y
                # push new weight
                heapq.heappush(self.heap, -new_weight)
        
        # return top of heap
        return -self.heap[0] if self.heap else 0
