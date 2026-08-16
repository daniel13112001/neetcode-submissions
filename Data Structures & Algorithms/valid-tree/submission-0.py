class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjList = {i:[] for i in range(n)}

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        if len(edges) < n - 1:
            return False

        visited = set()

        def hasCycle(node, parent):

            nonlocal visited

            if node in visited:
                return True

            visited.add(node)

            for nei in adjList[node]:
                if nei == parent:
                    continue
                if hasCycle(nei, node):
                    return True
            return False
        
        for node in adjList:
            if node not in visited and hasCycle(node, None):
                return False
        return True


    

        