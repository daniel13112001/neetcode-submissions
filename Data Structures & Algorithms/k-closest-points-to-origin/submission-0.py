

class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        ans = []

        for i, point in enumerate(points):

            dist = -((point[0] ** 2) + (point[1] ** 2))

            if len(heap) < k:
                heapq.heappush(heap, (dist, point))
            else:
                heapq.heappush(heap, (dist, point))
                heapq.heappop(heap)

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans


        