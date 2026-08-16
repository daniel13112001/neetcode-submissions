class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        buckets = [[] for i in range(len(nums))]

        for num, count in freq.items():
            buckets[count-1].append(num)

        count = 0
        ans = []
        print(buckets)
       
        for b in buckets[::-1]:
            if count >= k:
                break
            for i in b:
                ans.append(i)
            count += len(b)

        return ans
        