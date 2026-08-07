class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # initlaize num cycles
        num_cycles= 0
        self.n = n
        idle_count = 0

        # calculate frequencies of each task -> hashmap
        hashmap = {}
        for task in tasks:
            if task in hashmap:
                hashmap[task] += 1
            else:
                hashmap[task] = 1
        # initlaize and populate a max heap
        self.heap = []
        for count in hashmap.values():
            heapq.heappush(self.heap, -count)

        while self.heap:
            # temp list to store the new counts and push after while 
            temp = []
            # reset n
            n = self.n
            # reset idle_count
            idle_count = 0
            # pop max heap and execute first task
            first_task = -heapq.heappop(self.heap)
            # inc num_cycles
            num_cycles += 1
            if first_task -1 > 0:
                # store in temp
                temp.append(first_task -1)

            # while n
            while n:
                # dec n
                n -= 1
                # if heap is not empty
                if self.heap:
                    # execute task
                    # pop and exec next task
                    next_task = -heapq.heappop(self.heap)
                    # inc num_cycles
                    num_cycles += 1
                    if next_task -1 > 0:
                        temp.append(next_task -1)
                else:
                    # idle
                    idle_count += 1

            # after this cycle push back updated values
            for count in temp:
                heapq.heappush(self.heap, -count)
            if self.heap:
                num_cycles += idle_count


        return num_cycles


        