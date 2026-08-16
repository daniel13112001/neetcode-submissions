class Status:
        UNVISITED = -1
        VISITING = 0
        VISITED = 1

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = {}

        for u, v in prerequisites:
            if u not in adjList:
                adjList[u] = [v]
            else:
                adjList[u].append(v)

        state = [Status.UNVISITED] * numCourses 

        def hasCycle(node):

            if state[node] == Status.VISITED:
                return False
            
            if state[node] == Status.VISITING:
                return True

            state[node] = Status.VISITING

            for nei in adjList.get(node, []):
                if hasCycle(nei):
                    return True
            
            state[node] = Status.VISITED

            return False

        for node in adjList:
            if state[node] == Status.UNVISITED and hasCycle(node):
                return False
                
        return True



        