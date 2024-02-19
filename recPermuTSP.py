def permutations(data):
  if len(data)<=1:
    return[data]
  else:
    permutations_list=[]
    for i in range(len(data)):
      first = data[i]
      rest = data[:i] + data[i+1:]
      for permu in permutations(rest):
        if permu not in permutations_list:
            permutations_list.append([first]+permu)
    return permutations_list
  
class Graph:
    def __init__(self,V):
        self.V=V
        self.adj = {}
        self.adjMat = [[0]*V for _ in range(V)]

    def addEdge(self, u, v,weight):
        if u not in self.adj:
           self.adj[u]=[]
        if v not in self.adj:
            self.adj[v]=[]

        self.adj[u].append(v)
        self.adjMat[u][v]=weight

    def TSP(self, start, end):
        minCost=10000
        nodes = []
        for node in self.adj:
            nodes.append(node)

        permus = permutations(nodes)
        print(permus)
        selected_permus = []
        for perm in permus:
                if perm[0]==start and perm[-1]==end:
                    selected_permus.append(perm)
        
        print('selected',selected_permus)

        for path in selected_permus:
            print('path')
            path_cost=0
            for i in range(len(path)-1):
                path_cost+=self.adjMat[i][i+1]
                print(path_cost)
                if path_cost<minCost:
                    minCost=path_cost

        return minCost





    
    

g = Graph(4)
g.addEdge(0, 1,2)
g.addEdge(0, 2,3)
g.addEdge(0, 3,1)

g.addEdge(1,0, 2)
g.addEdge(1,2,4)
g.addEdge(1,3,3)

g.addEdge(2,0, 3)
g.addEdge(2,1,4)
g.addEdge(2,3,3)


g.addEdge(3,0, 1)
g.addEdge(3,1,2)
g.addEdge(3,2,3)

g.TSP(0,1)
