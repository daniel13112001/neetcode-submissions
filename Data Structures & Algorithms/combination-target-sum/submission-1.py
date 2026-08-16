class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        path = []

        def findCombinationSum(i, remaining):
            
            if i >= len(nums):
                return
            if remaining < 0:
                return
            if remaining == 0:
                ans.append(path[:])
                return

            # Choose i
            path.append(nums[i])
            findCombinationSum(i, remaining-nums[i])
            path.pop()

            # Dont choose i
            findCombinationSum(i+1, remaining)


        findCombinationSum(0, target)
        return ans
        