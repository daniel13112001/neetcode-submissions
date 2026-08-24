class Solution:
    def climbStairs(self, n: int) -> int:

        cache ={}

        def helper(n):

            if n == 1:
                return 1
            if n == 2:
                return 2

            if n-1 in cache:
                f = cache[n-1]
            else:
                f = helper(n-1)
                cache[n-1] = f
            
            if n-2 in cache:
                s = cache[n-2]
            else:
                s = helper(n-2)
                cache[n-2] = f

            return f + s

        return helper(n)

        

        