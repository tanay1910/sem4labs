from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.adjList = defaultdict(list)
        self.visited=[False] * V 
        self.invalidMoves = defaultdict(list)

    def addEdge(self,u,v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)


    def addBoundary(self, x,y):
        self.invalidMoves[x].append(y)
        self.invalidMoves[y].append(x)


    def dfs(self,node,goal):
        if self.visited[node]==False :
            self.visited[node]=True
            print(node)
            if node == goal:
                print('reached')
                return
            for neigh in self.adjList[node]:
                if neigh in self.invalidMoves[node]:
                    continue
                self.dfs(neigh,goal)


g = Graph(11)

g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(3,4)
g.addEdge(2,4)
g.addEdge(2,6)
g.addEdge(4,5)
g.addEdge(5,6)
g.addEdge(5,8)
g.addEdge(6,7)
g.addEdge(6,9)
g.addEdge(7,10)
g.addEdge(7,8)

g.addBoundary(1,2)
g.addBoundary(4,2)
g.addBoundary(6,2)
g.addBoundary(5,8)
g.dfs(1,8)




