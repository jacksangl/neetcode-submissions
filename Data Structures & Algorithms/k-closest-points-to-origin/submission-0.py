import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origins = []

        for point in points:
            dist = math.sqrt( pow(point[0], 2) + pow(point[1], 2))
            x, y = point[0], point[1]
            heapq.heappush(origins, (-dist, [x, y]))

            if len(origins) > k:
                heapq.heappop(origins)
        res = [origins[i][1] for i in range(k)]
        return res if res else None