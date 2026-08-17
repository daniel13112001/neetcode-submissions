class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res, path = [], []

        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n):
                path.append(i+1)
                backtrack(i+1, path)
                path.pop()


        backtrack(0, path)
        return res
        