from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # intilaize heap
        self.heap = []
        point_list = []

        # calcualte distance from origin
        for point in points:
            dist = (sqrt((point[0] - 0)**2 + (point[1] - 0)**2))
            # push each distance and coorinate pair as tuple to heap
            heapq.heappush(self.heap, (dist, point))

        # return top k coordinates with the smallets distance 
        while k:
            k -= 1
            point_list.append(heapq.heappop(self.heap)[1])


        return point_list

        