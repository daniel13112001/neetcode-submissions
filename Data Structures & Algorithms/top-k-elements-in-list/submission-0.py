class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        [2,2,3,1,0,2,4, 6. 3, 4]

        2 - 3
        3 - 2
        1 -1 
        4 - 2
        6 - 1
        0 - 1
        # Sort by count, then return top k. nlogn where n is length of nums 
        maxHeap 
        """

        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        heap = []
        

        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))
        
        topK = []
        for i in range(k):
            topK.append(heapq.heappop(heap)[1])
            
        return topK

        
        