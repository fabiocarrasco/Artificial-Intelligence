from asyncio.windows_events import NULL
from copy import deepcopy
from helpers import Node, NPuzzle, LEFT, RIGHT, UP, DOWN


def BFS(puzzle):
    """
    Breadth-First Search.

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    states_searched: An ordered list of all states searched.
    final_solution: An ordered list of moves representing the final solution.
    """

    states_searched = [Node(puzzle)]
    puzzles_searched = [puzzle.puzzle]
    final_solution = []
    queue = [Node(puzzle)]

    if not states_searched[-1].state.check_puzzle():
        while len(queue) != 0:
            parent_node = queue.pop(0)
            parent_state = parent_node.state
            new_state = deepcopy(parent_state)
            if parent_node.depth < 20:
                if  Check_State(parent_node,new_state,UP,puzzles_searched):
                    new_node = Node(new_state, parent_node, UP)
                    states_searched.append(new_node)
                    puzzles_searched.append(new_state.puzzle)
                    queue.append(new_node)
                    if states_searched[-1].state.check_puzzle():
                        break
                new_state = deepcopy(parent_state)
                if Check_State(parent_node,new_state,DOWN,puzzles_searched):
                    new_node = Node(new_state, parent_node, DOWN)
                    states_searched.append(new_node)
                    puzzles_searched.append(new_state.puzzle)
                    queue.append(new_node)
                    if states_searched[-1].state.check_puzzle():
                        break
                new_state = deepcopy(parent_state)
                if  Check_State(parent_node,new_state,LEFT,puzzles_searched):
                    new_node = Node(new_state, parent_node, LEFT)
                    states_searched.append(new_node)
                    puzzles_searched.append(new_state.puzzle)
                    queue.append(new_node)
                    if states_searched[-1].state.check_puzzle():
                        break
                new_state = deepcopy(parent_state)
                if  Check_State(parent_node,new_state,RIGHT,puzzles_searched):
                    new_node = Node(new_state, parent_node, RIGHT)
                    states_searched.append(new_node)
                    puzzles_searched.append(new_state.puzzle)
                    queue.append(new_node)
                    if states_searched[-1].state.check_puzzle():
                        break
    
    final_solution = states_searched[-1].moves
    return states_searched, final_solution


def DFS(puzzle):
    """
    Depth-First Search.

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    states_searched: An ordered list of all states searched.
    final_solution: An ordered list of moves representing the final solution.
    """

    states_searched = [Node(puzzle)]
    puzzles_searched = [puzzle.puzzle]
    final_solution = []
    counter = 0

    queue = [Node(puzzle)]

    
    if not states_searched[-1].state.check_puzzle():
        #while len(queue) != 0:
        while len(queue) != 0:
            parent_node = queue.pop(len(queue)-1)
            parent_state = parent_node.state
            new_state = deepcopy(parent_state)
            if counter != 0:
                puzzles_searched.append(parent_state.puzzle)
                states_searched.append(parent_node)
                if states_searched[-1].state.check_puzzle():
                    break
            if parent_node.depth <=50:
                if Check_State(parent_node,new_state,RIGHT,puzzles_searched):
                    new_node = Node(new_state, parent_node, RIGHT)
                    queue.append(new_node)
                new_state = deepcopy(parent_state)
                if Check_State(parent_node,new_state,LEFT,puzzles_searched):
                    new_node = Node(new_state, parent_node, LEFT)
                    queue.append(new_node)
                new_state = deepcopy(parent_state)
                if Check_State(parent_node,new_state,DOWN,puzzles_searched):
                    new_node = Node(new_state, parent_node, DOWN)
                    queue.append(new_node)
                new_state = deepcopy(parent_state)
                if Check_State(parent_node,new_state,UP,puzzles_searched):
                    new_node = Node(new_state, parent_node, UP)
                    queue.append(new_node)
            counter+=1
    final_solution = states_searched[-1].moves

    return states_searched, final_solution


def A_Star_H1(puzzle):
    """
    A-Star with Heuristic 1

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    states_searched: An ordered list of all states searched.
    final_solution: An ordered list of moves representing the final solution.
    """

    states_searched = [Node(puzzle)]
    puzzles_searched = [puzzle.puzzle]
    final_solution = []
    queue = [(Node(puzzle),Get_Heauristic1(Node(puzzle)))]
    counter = 0
    
    if not states_searched[-1].state.check_puzzle():
        while len(queue) != 0:
            sorted(queue, key=lambda queue: queue[1])
            parent_node = queue.pop(0)[0]
            parent_state = parent_node.state
            new_state = deepcopy(parent_state)
            if counter != 0:
                puzzles_searched.append(parent_state.puzzle)
                states_searched.append(parent_node)
                if states_searched[-1].state.check_puzzle():
                    break
            if  Check_State(parent_node,new_state,UP,puzzles_searched):
                new_node = Node(new_state, parent_node, UP)
                heauristic = Get_Heauristic1(new_node)
                queue.append((new_node,heauristic))
            new_state = deepcopy(parent_state)
            if Check_State(parent_node,new_state,DOWN,puzzles_searched):
                new_node = Node(new_state, parent_node, DOWN)
                heauristic = Get_Heauristic1(new_node)
                queue.append((new_node, heauristic))
            new_state = deepcopy(parent_state)
            if  Check_State(parent_node,new_state,LEFT,puzzles_searched):
                new_node = Node(new_state, parent_node, LEFT)
                heauristic = Get_Heauristic1(new_node)
                queue.append((new_node,heauristic))
            new_state = deepcopy(parent_state)
            if  Check_State(parent_node,new_state,RIGHT,puzzles_searched):
                new_node = Node(new_state, parent_node, RIGHT)
                heauristic = Get_Heauristic1(new_node)
                queue.append((new_node,heauristic))
            counter+=1
    
    final_solution = states_searched[-1].moves
    return states_searched, final_solution


def A_Star_H2(puzzle):
    """
    A-Star with Heauristic 2

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    states_searched: An ordered list of all states searched.
    final_solution: An ordered list of moves representing the final solution.
    """

    states_searched = [Node(puzzle)]
    puzzles_searched = [puzzle.puzzle]
    final_solution = []
    queue = [(Node(puzzle),Get_Heauristic1(Node(puzzle)))]
    counter = 0

    
    if not states_searched[-1].state.check_puzzle():
        while len(queue) != 0:
            sorted(queue, key=lambda queue: queue[1])
            parent_node = queue.pop(0)[0]
            parent_state = parent_node.state
            new_state = deepcopy(parent_state)
            if counter != 0:
                puzzles_searched.append(parent_state.puzzle)
                states_searched.append(parent_node)
                if states_searched[-1].state.check_puzzle():
                    break
            if parent_node.depth <=20:
                if  Check_State(parent_node,new_state,UP,puzzles_searched):
                    new_node = Node(new_state, parent_node, UP)
                    heauristic = Get_Heauristic2(new_node)
                    queue.append((new_node,heauristic))
                new_state = deepcopy(parent_state)
                if Check_State(parent_node,new_state,DOWN,puzzles_searched):
                    new_node = Node(new_state, parent_node, DOWN)
                    heauristic = Get_Heauristic2(new_node)
                    queue.append((new_node, heauristic))
                new_state = deepcopy(parent_state)
                if  Check_State(parent_node,new_state,LEFT,puzzles_searched):
                    new_node = Node(new_state, parent_node, LEFT)
                    heauristic = Get_Heauristic2(new_node)
                    queue.append((new_node,heauristic))
                new_state = deepcopy(parent_state)
                if  Check_State(parent_node,new_state,RIGHT,puzzles_searched):
                    new_node = Node(new_state, parent_node, RIGHT)
                    heauristic = Get_Heauristic2(new_node)
                    queue.append((new_node,heauristic))
                counter+=1
    
    final_solution = states_searched[-1].moves
    return states_searched, final_solution

def Get_Heauristic1(parent_node):
    '''
    Heauristic Helper Function 1
    
    Arguments:
    - parent_node: Node object representing a puzzle.
    
    Retruns:
    - heauristic: An integer number representing heauristic using number of misplaced tiles for parent_node puzzle.
    '''
    heauristic = len(parent_node.moves)
    parent_state = parent_node.state
    size = parent_state.size-1
    counter =  1
    for x in range(size):
        for y in range(size):
            if parent_state.puzzle[x][y] == counter:
                heauristic += 1
            counter+=1
            if counter == size*size+1:
                counter = 0
    return heauristic

def Get_Heauristic2(parent_node):
    '''
    Heauristic Helper Function 2
    
    Arguments:
    - parent_node: Node object representing a puzzle.
    
    Returns:
    - heauristic: An integer number representing heauristic using manhattan distance for parent_node puzzle.
    '''
    heauristic = -len(parent_node.moves)
    parent_state = parent_node.state
    size = parent_state.size-1
    counter = 1
    count_dict = {}
    for x in range(size):
        for y in range(size):
            count_dict[counter] = (x, y)
            counter+=1
            if counter+1 == size*size+1:
                counter = 0
    counter = 1
    for x in range(size):
        for y in range(size):
            if parent_state.puzzle[x][y] == counter:
                pass
            else:
                x1, y1 = count_dict.get(counter)
                heauristic -= abs(x - x1)
                heauristic -= abs(y - y1)
            counter += 1
            if counter+1 == size*size+1:
                counter = 0
    return heauristic

def Check_State(parent,child,direction,puzzles):
    '''
    State Validity Helper 
    
    Arguments:
    - parent: represents parent node
    - child: represents child node
    - puzzles: represents list of searched puzzles
    Returns:
    - A boolean value representing the validity of movement from parent to child.
    '''
    if direction==DOWN:
        return parent.state.zero[0] != 0 and child.swap(parent.state.zero[0],parent.state.zero[1],parent.state.zero[0]-1,parent.state.zero[1]) not in puzzles and (parent.moves == [] or parent.moves[-1] != UP)
    elif direction==UP:
        return parent.state.zero[0] != parent.state.size-1 and child.swap(parent.state.zero[0],parent.state.zero[1],parent.state.zero[0]+1,parent.state.zero[1]) not in puzzles and (parent.moves == [] or parent.moves[-1] != DOWN) 
    elif direction==RIGHT:
        return parent.state.zero[1] != 0 and child.swap(parent.state.zero[0],parent.state.zero[1],parent.state.zero[0],parent.state.zero[1]-1) not in puzzles and (parent.moves == [] or parent.moves[-1] != LEFT)
    elif direction==LEFT:
        return parent.state.zero[1] != parent.state.size-1 and child.swap(parent.state.zero[0],parent.state.zero[1],parent.state.zero[0],parent.state.zero[1]+1) not in puzzles and (parent.moves == [] or parent.moves[-1] != RIGHT)
    