class Node:
    def __init__(self, state, parent, g_cost, h_cost):
        self.state=state
        self.parent=parent
        self.g_cost=g_cost
        self.h_cost=h_cost
        self.f_cost=self.g_cost+self.h_cost

def giveHCost(curr_state,final_state):
    count=0
    for i in range(len(curr_state)):
        if curr_state[i]!=final_state[i] and curr_state[i]!=0:
            count+=1
    return count

def gen_neighbours(state):
    neighbours=[]
    blank_index = state.index(0)
    row,col = blank_index // 3, blank_index %3
    if row > 0 :
        new_state = list(state)
        new_state[blank_index], new_state[blank_index-3] = new_state[blank_index-3], new_state[blank_index]
        neighbours.append(new_state)
    if row < 2:
        new_state = list(state)
        new_state[blank_index], new_state[blank_index + 3] = new_state[blank_index + 3], new_state[blank_index]
        neighbours.append(new_state)
    # Left
    if col > 0:
        new_state = list(state)
        new_state[blank_index], new_state[blank_index - 1] = new_state[blank_index - 1], new_state[blank_index]
        neighbours.append(new_state)
    # Right
    if col < 2:
        new_state = list(state)
        new_state[blank_index], new_state[blank_index + 1] = new_state[blank_index + 1], new_state[blank_index]
        neighbours.append(new_state)
    return neighbours
    

def eightPuzzle(start_state, end):
    frontier = [Node(start_state, None, 0, giveHCost(start_state,goal_state))]
    explored = set()

    while frontier:
        min_fcost_index=0
        for i  in range(len(frontier)) :
            if frontier[i].f_cost<frontier[min_fcost_index].f_cost:
                min_fcost_index=i

        for item in frontier:
            print(item.state)
        
        curr_node = frontier.pop(min_fcost_index)

        if curr_node.state == end.state:
            print('found')
            print(curr_node.state)
            break

        if curr_node not in explored:
            explored.add(curr_node)
            for neigh in gen_neighbours(start_state):
                neigh_node = Node(neigh, curr_node, curr_node.g_cost+1, giveHCost(neigh,end.state))
                if neigh_node not in explored and neigh_node not in frontier:
                    frontier.append(neigh_node)
                elif neigh_node in frontier:
                    for i, node in enumerate(frontier):
                        if node.state == neigh_node.state and node.f_cost<neigh_node.f_cost:
                            node.f_cost=neigh_node.f_cost
        




start_state = [1, 0, 3,
                8, 2, 4, 
                7, 6, 5]
goal_state = [1, 2, 3, 
              8, 0, 4, 
              7, 6, 5]

eightPuzzle(start_state, Node(goal_state, None, 0 , 0 ))

