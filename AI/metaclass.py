from AI_Interactions import AIInteractions


class AIBase:
    pass


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def basic_heuristic(state, problem: AIInteractions = None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return problem.get_state_score(state)


def basic_heuristic_2(state, problem: AIInteractions = None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return problem.get_state_score(state)


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


def a_star_search(problem: AIInteractions, node_search_quota=10000, heuristic=null_heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # get starting point
    board_instance = problem.get_next_start_state()
    queue = problem.get_successors(board_instance)
    # make a visited list, paternity list
    visited = set(x for (x, y, z) in queue)
    father = {}
    g = lambda x: x[2] + heuristic(x[0], problem)  # x = (curr_state, curr_move, score), where the current state is the state *after* curr_move has been executed, and the score is also after the move.
    i = 0
    while len(queue):
        curr_state, curr_move, score = queue.pop()  # reversed from min to max (score)
        if node_search_quota == i:
            path = []
            while (curr_state, curr_move) in father.keys():
                path.insert(0, curr_move)
                curr_state, curr_move = father[(curr_state, curr_move)]
            path.insert(0, curr_move)
            return path
        for (bstate, bmove, reward) in problem.get_successors(curr_state):  # TODO alternatively, modify A* to get the successors of currstate+curr+move instead of currstate being prevstate + currmove.
            if bstate not in visited:
                queue_elem = (bstate, bmove, reward + score)
                queue.insert(find_loc(g, queue, queue_elem), queue_elem)
                visited.add(bstate)
                if (bstate, bmove) not in father:
                    father[(bstate, bmove)] = (curr_state, curr_move)
        i += 1
    return []
