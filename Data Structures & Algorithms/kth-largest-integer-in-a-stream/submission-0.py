class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        # build heap from nums
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        # add to the stream in heap
        heapq.heappush(self.heap, val)
        
        # if val > root of heap:
        if len(self.heap) > self.k:
            # pop from heap 
            heapq.heappop(self.heap)


        # return whats popped
        return self.heap[0]
        
