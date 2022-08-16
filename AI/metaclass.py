class AIBase:
    pass


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def find_loc(func, arr, element):
    l = 0
    h = len(arr)
    element_val = func(element)
    while h > l:
        m = (h + l) // 2
        mval = func(arr[m])
        if mval < element_val:
            l = m + 1
        else:
            h = m
    return l


# reverse from min to max (score), make
def a_star_search(problem, node_search_quota = 10000, heuristic=null_heuristic):
    """
   Search the node that has the lowest combined cost and heuristic first.
   """
    # get starting point
    board_instance: board.Board = problem.get_start_state()
    queue = problem.get_successors(board_instance)
    # make a visited list, paternity list
    visited = set(x for (x, y, z) in queue)
    father = {}
    g = lambda x: x[2] + heuristic(x[0], problem)
    i = 0
    while len(queue):
        curr_state, curr_move, score = queue.pop(0)
        if node_search_quota == i:
            path = []
            while (curr_state, curr_move) in father.keys():
                path.insert(0, curr_move)
                curr_state, curr_move = father[(curr_state, curr_move)]
            path.insert(0, curr_move)
            return path
        for (bstate, bmove, reward) in problem.get_successors(curr_state):
            if bstate not in visited:
                queue.insert(
                    find_loc(g, queue, (bstate, bmove, reward + score)),
                    (bstate, bmove, reward + score))
                visited.add(bstate)
                if (bstate, bmove) not in father:
                    father[(bstate, bmove)] = (curr_state, curr_move)
        i += 1
    return []


