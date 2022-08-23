from typing import Tuple

import Game


class AIBase:
    pass


def null_heuristic(state: Game, action: Tuple[Tuple[int, int], bool]):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def basic_heuristic(state: Game, action: Tuple[Tuple[int, int], bool]):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return state.get_state_score() + 10000*state.get_not_move(action)



def basic_heuristic_2(state: Game, action: Tuple[Tuple[int, int], bool]):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return state.get_state_score(state)

def predict_shoot_heuristic(state: Game, action: Tuple[Tuple[int, int], bool]):
    return state.predict_projectiles_Score()


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


def a_star_search(problem: Game, node_search_quota=10000,
                  heuristic=null_heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    queue = problem.get_successors()
    visited = set(x for (x, y, z) in queue)
    father = {}
    g = lambda x: x[2] + heuristic(x[0],
                                   x[1])  # x = (curr_state, curr_move, score), where the current state is the state *after* curr_move has been executed, and the score is also after the move.
    i = 0
    while len(queue):
        curr_state, curr_move, score = queue.pop()  # reversed from min to max (score)
        print(len(queue), [i for i in range(len(queue)) if queue[i][1][0] == [0, 0]])
        if node_search_quota == i:
            path = []
            key = get_key(curr_state, curr_move)
            while key in father.keys():
                path.append(curr_move)
                curr_state, curr_move = father[key]
                key = get_key(curr_state, curr_move)
            path.append(curr_move)
            return path
        for (bstate, bmove, reward) in problem.get_successors():  # TODO alternatively, modify A* to get the successors of currstate+curr+move instead of currstate being prevstate + currmove.
            if bstate not in visited:
                queue_elem = (bstate, bmove, reward + score)
                queue.insert(find_loc(g, queue, queue_elem), queue_elem)
                visited.add(bstate)
                key = get_key(bstate, bmove)
                if key not in father:
                    father[key] = (curr_state, curr_move)
        i += 1
    return []


def get_key(state, move):
    return state, (tuple(move[0]), move[1])


def a_star_player(problem: Game):
    next_moves = a_star_search(problem, node_search_quota=5, heuristic=predict_shoot_heuristic)
    if next_moves is []:
        return
    return next_moves
