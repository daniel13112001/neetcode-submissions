class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = []


        def generateSubsets(i, path):

            if i == len(nums):
                results.append(path[:])
                return 
            
            path.append(nums[i])
            generateSubsets(i+1, path)
            path.pop()

            generateSubsets(i+1, path)

        generateSubsets(0, [])

        return results

           
        