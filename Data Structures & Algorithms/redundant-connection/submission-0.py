class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) #Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return
        if self.rank[rootX] < self.rank[rootY]:
            rootX, rootY = rootY, rootX
        self.parent[rootY] = rootX
        if self.rank[rootX] == self.rank[rootY]:
            self.rank[rootX] += 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        f = UnionFind(len(edges))

        for u, v in edges:
            rootU, rootV = f.find(u-1), f.find(v-1)
            if rootU == rootV:
                return [u,v]
            f.union(u-1,v-1)
        
        