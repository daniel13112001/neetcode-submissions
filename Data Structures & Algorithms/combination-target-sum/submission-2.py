class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        results = []

        def findCombinations(i, path):

            if sum(path) == target:
                results.append(path[:])
                return 

            if sum(path) > target or i == len(nums):
                return 

            path.append(nums[i])
            findCombinations(i, path)

            path.pop()
            findCombinations(i+1, path)

        findCombinations(0, [])

        return results

        



            
        