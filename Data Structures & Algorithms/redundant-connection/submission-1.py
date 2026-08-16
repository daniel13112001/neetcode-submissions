class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootA, rootB = self.find(x), self.find(y)
        if rootA == rootB:
            return self.parent[rootA]
        if self.rank[rootA] < self.rank[rootB]:
            rootA, rootB = rootB, rootA
        if self.rank[rootA] == self.rank[rootB]:
            self.rank[rootA] += 1
        self.parent[rootB] = rootA


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        f = UnionFind(len(edges))

        for u, v in edges:
            if f.find(u-1) == f.find(v-1):
                return [u,v]
            f.union(u-1, v-1)


        return []
        