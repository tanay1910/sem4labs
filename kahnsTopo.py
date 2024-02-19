class Graph:
    def __init__(self, V):
        self.V=V
        self.adjMat = {}

    def addEdge(self, u, v):
        if u not in self.adjMat:
            self.adjMat[u]=[]
        if v not in self.adjMat:
            self.adjMat[v]=[]
        self.adjMat[u].append(v)

    def printAdjList(self):
        print(self.adjMat)

    def kahnsTopo(self):
        indegree={}
        for node in self.adjMat:
            indegree[node]=0
        for node in self.adjMat:
            for neigh in self.adjMat[node]:
                if neigh not in indegree:
                    indegree[neigh]=0
                indegree[neigh]+=1
        
        q=[]

        for node in indegree:
            if indegree[node]==0:
                q.append(node)

        
        while(q):
            curr=q.pop(0)
            print(curr)
            for neigh in self.adjMat[curr]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)

        



g=Graph(6)
g.addEdge(5,0)
g.addEdge(5,2)
g.addEdge(4,0)
g.addEdge(4,1)
g.addEdge(2,3)
g.addEdge(3,1)
g.kahnsTopo()