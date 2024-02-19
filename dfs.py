from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.adjList = defaultdict(list)
        self.visited=[False] * V 

    def addEdge(self,u,v):
        self.adjList[u].append(v)

    def dfs(self,node):
        if self.visited[node]==False :
            self.visited[node]=True
            print(node)
            for neigh in self.adjList[node]:
                self.dfs(neigh)

    def isCYCLIC(self, node):
        if self.visited[node]==True:
            print('cycle detected!')
        if self.visited[node]==False :
            self.visited[node]=True
            print(node)
            for neigh in self.adjList[node]:
                self.dfs(neigh)
        


    def DFSstack(self, node):
        stack =[node]
        visited = [0]*self.V
        
        while stack:
            curr = stack.pop()
            print(curr)
            if visited[curr]==False:
                visited[curr]=1
                for neigh in self.adjList[curr]:
                    self.DFSstack(neigh)

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


# print(g.visited)
# g.dfs(1)
g.DFSstack(1)
g.isCYCLIC(1)