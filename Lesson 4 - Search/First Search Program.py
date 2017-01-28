# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    destination = True
    path = True
    
    state = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    state[0][0] = 1
    
    cell_h = init[0]
    cell_v = init[1]
    g = 0
    
    current_state = [[g, cell_h, cell_v]]
    
    while destination and path:
        
        current_state.sort()
        current_state.reverse()
        index_n = current_state.pop()
        
        g = index_n[0]
        cell_h = index_n[1]
        cell_v = index_n[2]
        
        if (cell_h == goal[0] and cell_v == goal[1]):
            destination = False
        
        else:
            if len(current_state) == 0:
                path = False
                #print 'Destination not reachable'
            else:
                for i in delta:
                    cell_h_n = cell_h + i[0]
                    cell_v_n = cell_v + i[1]
                    if (cell_h_n >= 0 and cell_h_n < len(state)) and (cell_v_n >= 0 and cell_v_n < len(state[0])):
                        if state[cell_h_n][cell_v_n] == 0 and grid[cell_h_n][cell_v_n] == 0:
                            g_n = g + cost
                            current_state.append([g_n, cell_h_n, cell_v_n])
                            state[cell_h_n][cell_v_n] = 1
            
    return index_n

print search(grid,init,goal,cost)