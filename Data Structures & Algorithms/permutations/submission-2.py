class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res, path = [], []
        used = [False] * len(nums)


        def backtrack(start):

            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(start, len(nums)):
                if used[i]:
                    continue 
                path.append(nums[i])
                used[i] = True
                backtrack(0)
                path.pop()
                used[i] = False
               
    


        backtrack(0)
        return res
        