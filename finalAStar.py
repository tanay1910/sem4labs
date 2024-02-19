class  Graph:
    def __init__(self,V):
        self.V=V
        self.adjList = {}
        self.adjMat = [[0]*V for _ in range(V)]
        self.heuristics = {}
    
    def addEdge(self, u , v, cost):
        if u not in self.adjList:
            self.adjList[u]=[]
        self.adjList[u].append(v)
        self.adjMat[u][v]=cost
        if v not in self.adjList:
            self.adjList[v]=[]

    def addHeuristics(self):
        for node in self.adjList:
            hue_node = int(input(f"enter heu for {node}: "))
            self.heuristics[node]=hue_node
    
    def astartSearch(self, start, goal):
        frontier = [(self.heuristics[start], start)]
        visited = set()

        while frontier:
            frontier = sorted(frontier)
            print(frontier)
            [curr_cost, curr_node] = frontier.pop(0)

            if curr_node==goal:
                print('goal found')
                break

            visited.add(curr_node)

            for neigh in self.adjList[curr_node]:
                if neigh not in visited:
                    frontier.append((curr_cost+self.adjMat[curr_node][neigh]+self.heuristics[neigh],neigh))



g = Graph(6)
g.addEdge(0,1,1)
g.addEdge(1,4,2)
g.addEdge(4,5,3)
g.addEdge(1,3,3)
g.addEdge(3,5,1)
g.addEdge(0,2,3)
g.addEdge(2,5,3)
g.addHeuristics()
g.astartSearch(0,5)