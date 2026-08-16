class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        comps = {}

        for i, num in enumerate(nums):
            c = target - num 
            if c in comps:
                return [comps[c], i]
            comps[num] = i 
        return []
            
