class Solution:
    def rob(self, nums: List[int]) -> int:


        cache = {}
        def robbery(i):

            print(i)
            if i >= len(nums) or i < 0:
                return 0 
            
            if i == len(nums):
                return nums[i]
            
            if i in cache:
                return cache[i]
                      
            res =  max((nums[i]+robbery(i+2)), robbery(i+1))
            cache[i] = res 
            return res

        return robbery(0)
            
        