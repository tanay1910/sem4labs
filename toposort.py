from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.adjList = defaultdict(list)
        self.visited=[False] * V 
        self.topo=[]

    def addEdge(self,u,v):
        self.adjList[u].append(v)

    def dfs(self,node):
        if self.visited[node]==False :
            self.visited[node]=True
            print(node)
            self.topo.append(node)
            for neigh in self.adjList[node]:
                self.dfs(neigh)

g = Graph(11)
g.addEdge(1,2)
g.addEdge(1,7)
g.addEdge(7,9)
g.addEdge(2,4)
g.addEdge(4,5)
g.addEdge(4,6)

g.addEdge(7,8)
g.addEdge(7,10)
g.addEdge(2,3)


g.dfs(1)

print(g.topo[::-1])
