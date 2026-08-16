class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        sol = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if not stack:
                stack.append((i,t))
            else:
                top = stack[-1]
                while stack and t > top[1]:
                    sol[top[0]] = i - top[0]
                    stack.pop()
                    if stack:
                        top = stack[-1]
                stack.append((i,t))
        return sol

        