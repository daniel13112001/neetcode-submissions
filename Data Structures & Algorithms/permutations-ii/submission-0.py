class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res, path = [], []
        used = [False] * len(nums)
        seen = set()

        def backtrack():

            if len(path) == len(nums) and tuple(path) not in seen:
                res.append(path[:])
                seen.add(tuple(path))
                return 

            for i in range(len(nums)):
                if used[i]:
                    continue 
                path.append(nums[i])
                used[i] = True 
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return res
        