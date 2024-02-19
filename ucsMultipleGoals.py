class Graph:
    def __init__(self, V):
        self.V=V
        self.adjMat = {}

    def addEdge(self, u, v,cost):
        if u not in self.adjMat:
            self.adjMat[u]=[]
        self.adjMat[u].append((v,cost))

    def printAdjList(self):
        print(self.adjMat)

    def UCS(self, start, goals):
        frontier = []
        explored = []
        frontier.append((0,start,[]))
        path_to_goals = {}

        while frontier:
            frontier=sorted(frontier)
            [curr_cost, curr_node, path]=frontier.pop(0)

            if curr_node in explored:
                continue

            path = path+ [curr_node]

            if curr_node in goals:
                path_to_goals[curr_node] = path
                goals.remove(curr_node)

                if not goals: #all goals reached
                    print('all destination nodes found')
                    return path_to_goals

            
            for (neigh_node, neigh_cost) in self.adjMat[curr_node]:
                frontier.append((curr_cost+neigh_cost, neigh_node, path))




g = Graph(3)
g.addEdge('A',1,2)
g.addEdge('A',3,5)
g.addEdge(3,1,5)
g.addEdge(1,6,1)
g.addEdge(3,6,6)
g.addEdge(3,4,2)
g.addEdge(2,1,4)
g.addEdge(6,4,7)
g.addEdge(4,2,4)
g.addEdge(4,5,3)
g.addEdge(5,2,6)
g.addEdge(5,6,3)
# g.printAdjList()

paths=g.UCS('A',[6,5])
print(paths)