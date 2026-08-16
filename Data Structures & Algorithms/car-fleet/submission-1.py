class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [(p, s) for p,s in zip(position, speed)]
        cars.sort()
        stack = []

        end = len(cars) - 1
        for i in range(end, -1, -1):
            position = cars[i][0]
            speed = cars[i][1]
            timeNeeded = (target - position) / speed
            if not stack:
                stack.append(timeNeeded)
            else:
                if timeNeeded > stack[-1]:
                    stack.append(timeNeeded)
        return len(stack)


        


        

        