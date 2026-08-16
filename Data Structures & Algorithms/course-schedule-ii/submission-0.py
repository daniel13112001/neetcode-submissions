class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjList = {i:[] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            adjList[prereq].append(course)

        inDegrees = {i:0 for i in range(numCourses)}

        for node in adjList:
            for nei in adjList.get(node, []):
                inDegrees[nei] += 1

        q = deque()
        ordering = []
        # Push sources (in-degree == 0) onto the queue

        for node in inDegrees:
            if inDegrees[node] == 0:
                q.append(node)
                ordering.append(node)

        while q:
            course = q.popleft()
            for nei in adjList[course]:
                inDegrees[nei] -= 1
                if inDegrees[nei] == 0:
                    q.append(nei)
                    ordering.append(nei)

        if len(ordering) == numCourses:
            return ordering
        return []



                
