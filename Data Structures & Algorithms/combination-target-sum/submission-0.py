class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        path = []

        def findCombination(i, remaining):

            if remaining == 0:
                ans.append(path[:])
                return

            if i == len(nums):
                return
            
            if remaining < 0:
                return

            # Skip i
            findCombination(i+1, remaining)

            # Choose i
            path.append(nums[i])
            findCombination(i, remaining-nums[i])
            path.pop()

        findCombination(0, target)

        return ans 
        