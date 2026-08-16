class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjList = {i:[] for i in range(n)}

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()

        def dfs(node) -> None:

            nonlocal visited

            if node in visited:
                return
            visited.add(node)

            for nei in adjList[node]:
                dfs(nei)
        
        cc = 0
        for node in adjList:
            if node not in visited:
                cc += 1
                dfs(node)
        
        return cc



        
        