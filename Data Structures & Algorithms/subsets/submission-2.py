class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        path = []

        def generateSubsets(i):

            if i == len(nums):
                ans.append(path[:])
                return
            
            path.append(nums[i])
            generateSubsets(i+1)
            path.pop()

            generateSubsets(i+1)

        generateSubsets(0)
        return ans



        