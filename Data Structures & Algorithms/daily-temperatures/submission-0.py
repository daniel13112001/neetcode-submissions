class Solution:

    def dailyTemperatures(self, t: List[int]) -> List[int]:

        ret = [0] * len(t)
        stack = [(0, t[0])] # Store value, index

        for idx, temp in enumerate(t):
            while stack and temp > stack[-1][1]: # It is the solution for stack top
                ret[stack[-1][0]] = (idx-stack[-1][0])
                stack.pop()
            stack.append((idx, temp))

        return ret


        