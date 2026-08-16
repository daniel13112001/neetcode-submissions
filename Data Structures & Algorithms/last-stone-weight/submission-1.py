import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-stone for stone in stones]

        heapq.heapify(stones)


        while len(stones) > 1:

            largest = -heapq.heappop(stones)
            secondLargest = -heapq.heappop(stones)

            if largest == secondLargest:
                continue
            heapq.heappush(stones, -(largest-secondLargest))
        
        return -stones[0] if len(stones) == 1 else 0