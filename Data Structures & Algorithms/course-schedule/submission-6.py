class Status:
    UNVISITED = -1
    INPROGRESS = 0
    COMPLETED = 1


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = {i:[] for i in range(numCourses)}

        for u, v in prerequisites:
            adjList[v].append(u)

        
        state = [Status.UNVISITED] * numCourses
        print(state)

        def hasCycle(node):

            if state[node] == Status.COMPLETED:
                return False

            if state[node] == Status.INPROGRESS:
                return True
            
            state[node] = Status.INPROGRESS

            for nei in adjList[node]:
                if hasCycle(nei):
                    return True

            state[node] = Status.COMPLETED
            return False
            

        for node in adjList:
            if hasCycle(node):
                return False

        return True

        