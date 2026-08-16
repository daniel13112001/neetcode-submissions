class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = 0
        fast = 0

        while True:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
            if fast == slow:
                break

        slow = 0

        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow


        