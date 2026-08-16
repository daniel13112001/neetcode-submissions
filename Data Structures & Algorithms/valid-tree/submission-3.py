class Status:
    VISITED = 1
    UNVISITED = -1

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        adjList = {i:[] for i in range(n)}
        

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        print(adjList)

        state = [Status.UNVISITED] * n 

        def dfs(node, parent):

            if state[node] == Status.VISITED:
                return False
            
            state[node] = Status.VISITED
            
            for nei in adjList[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

            return True
    

        for i in range(n):
            if state[i] == Status.UNVISITED:
                if not dfs(i, -1):
                    return False
        return True

        