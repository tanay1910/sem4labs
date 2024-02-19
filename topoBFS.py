from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.adjList = defaultdict(list)
        self.visited=[False] * V 
        self.inDegree=[0]*self.V

    def addEdge(self,u,v):
        self.adjList[u].append(v)
        self.inDegree[v]+=1

    def dfs(self,node):
        if self.visited[node]==False :
            self.visited[node]=True
            print(node)
            for neigh in self.adjList[node]:
                self.dfs(neigh)

    def bfs(self, node):
        visited = [0]*self.V
        qf = []
        qf.append(node)
        while qf:
            curr = qf.pop(0)
            print(curr)
            for neigh in self.adjList[curr]:
                qf.append(neigh)

    def topoBFS(self):
        visited=[0]*self.V
        qf=[node for node in range(1,self.V) if self.inDegree[node]==0]
        topoOrder=[]
        while qf:
            curr = qf.pop(0)
            print(curr)
            for neigh in self.adjList[curr]:
                # print('neigh', neigh)
                self.inDegree[neigh]-=1
                if self.inDegree[neigh]==0:
                    topoOrder.append(qf)



g = Graph(11)
g.addEdge(1,2)
g.addEdge(2,7)
g.addEdge(1,10)
g.addEdge(1,7)
g.addEdge(7,9)
g.addEdge(2,4)
g.addEdge(4,5)
g.addEdge(4,6)

g.addEdge(7,8)
g.addEdge(7,10)
g.addEdge(2,3)

g.topoBFS()