class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Are there identical numbers within k of each other?

        l = 0
        r = 0
        seenInWindow = set()

        while r < len(nums): 
            if r - l > k:
                seenInWindow.remove(nums[l])
                l += 1
            if nums[r] in seenInWindow:
                return True
            seenInWindow.add(nums[r])
            r += 1

        return False


        