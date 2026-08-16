class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1
        last = nums[len(nums) - 1]
        mid = 0


        while low <= high:
            middle = (low + high) // 2
            if nums[middle] <= last:
                high = middle - 1
                mid = middle
            else:
                low = middle + 1

        # If mid = 0, then there is only one array to search

        print(mid)
        # Array boundaries
        arr1_low = 0
        if mid > 0:
            arr1_high = mid - 1
            arr2_low = mid
            arr2_high = len(nums) - 1
        else:
            arr1_high = len(nums) - 1
            arr2_high = -1
            arr2_low = -1
        print(arr1_low, arr1_high)
        print(arr2_low, arr2_high)

        # Decide which array to search:

        if arr2_low == -1 or arr2_high == -1:
            found, idx = self.binSearch(nums, target, arr1_low, arr1_high)
        elif target >= nums[arr1_low] and target <= nums[arr1_high]:
            found, idx =  self.binSearch(nums, target, arr1_low, arr1_high)
        else:
            found, idx =  self.binSearch(nums, target, arr2_low, arr2_high)
        
        if found:
            return idx
        else:
            return -1

    def binSearch(self, nums, target, low, high):


        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return (True, mid)
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return (False, -1)
    
        

        

        