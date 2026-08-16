class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []

        for i, num in enumerate(nums):
            
            if i < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappush(heap, num)
                heapq.heappop(heap)

        return heap[0]