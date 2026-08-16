class Solution:

    def findMin(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1
        last = nums[high]
        ans = nums[0]

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= last:
                ans = nums[mid]  
                high = mid - 1       
            else:
                low = mid + 1
        return ans

        
        