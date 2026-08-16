class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        path = []
        ans = []

        def generateSubsets(i):

            if i == len(nums):
                ans.append(path[:])
                return
            
            # Don't pick i
            generateSubsets(i+1)

            # Pick i
            path.append(nums[i])
            generateSubsets(i+1)
            # Undo pick i
            path.pop()

        generateSubsets(0)
        return ans

        