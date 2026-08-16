class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjList = {i:[] for i in range(numCourses)}
        order = []
        q = deque([])

        for u, v in prerequisites:
            adjList[v].append(u)
        
        inDegrees = {i:0 for i in range(numCourses)}

      

        for u, v in prerequisites:
                inDegrees[u] += 1

        # All source vertices
        for i in range(len(inDegrees)):
            if inDegrees[i] == 0:
                q.append(i)

        while q:
            cur = q.popleft()
            order.append(cur)
            for n in adjList[cur]:
                inDegrees[n] -= 1
                if inDegrees[n] == 0:
                    q.append(n)

        if len(order) == numCourses:
            return order
        return []
           
        