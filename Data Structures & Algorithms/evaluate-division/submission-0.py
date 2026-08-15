class UnionFind:
    def __init__(self):
        self.parent = {}
        self.weight = {}

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.weight[x] = 1.0

    def find(self, x):
        if x != self.parent[x]:
            prev_parent = self.parent[x]
            self.parent[x] = self.find(prev_parent)
            self.weight[x] *= self.weight[prev_parent]
        return self.parent[x]

    def union(self, x, y, value):
        self.add(x)
        self.add(y)
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.weight[root_x] = value * self.weight[y] / self.weight[x]

    def getRatio(self, x, y):
        if x not in self.parent or y not in self.parent or self.find(x) != self.find(y):
            return -1.0
        return self.weight[x] / self.weight[y]

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ufset = UnionFind()

        for (a,b), value in zip(equations, values):
            ufset.union(a, b, value)

        return [ufset.getRatio(x,y) for x, y in queries]

