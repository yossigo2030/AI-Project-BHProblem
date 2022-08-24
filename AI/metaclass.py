from typing import Tuple

import Game
import math
import Draw


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
    return 10000 * state.get_not_move(action)


def basic_heuristic_2(state: Game, action: Tuple[Tuple[int, int], bool]):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return state.get_state_score(state)


def predict_shoot_heuristic(state: Game, action: Tuple[Tuple[int, int], bool], depth=10):
    return state.predict_projectiles_Score(depth)


def stay_Alive(state: Game, action: Tuple[Tuple[int, int], bool]):
    return state.get_lives() * 1000


def Stay_Alive_Aim_To_Kill(state: Game, action: Tuple[Tuple[int, int], bool]):
    return stay_Alive(state, action) + 100*predict_shoot_heuristic(state, action, depth = 0)


def centerize(state: Game, action: Tuple[Tuple[int, int], bool]):
    location = [action[0][0]*state.player.speed + state.player.location[0], action[0][1]*state.player.speed + state.player.location[1]]
    dis = - 5 * distance(location , (Draw.WIDTH//2,Draw.LENGTH//2))
    print(dis)
    return dis

def distance(point1, point2):
    return math.sqrt(math.pow(point2[0] - point1[0],
                              2) + math.pow(
        point2[1] - point1[1], 2))


def centerize_alive(state: Game, action: Tuple[Tuple[int, int], bool]):
    return stay_Alive(state, action) + centerize(state, action)



def find_loc(func, arr, element):
    l = 0
    h = len(arr)
    element_val = func(element)
    while h > l:
        m = (h + l) // 2
        mval = func(arr[m])
        if mval > element_val:
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
    g = lambda x: x[2] + heuristic(x[0], x[1])  # x = (curr_state, curr_move, score), where the current state is the state *after* curr_move has been executed, and the score is also after the move.
    i = 0
    while len(queue):
        curr_state, curr_move, score = queue.pop(0)  # reversed from min to max (score)
        # print(len(queue), [i for i in range(len(queue)) if queue[i][1][0] == [0, 0]])
        if node_search_quota == i:
            path = []
            key = get_key(curr_state, curr_move)
            while key in father.keys():
                path.insert(0, curr_move)
                curr_state, curr_move = father[key]
                key = get_key(curr_state, curr_move)
            path.insert(0, curr_move)
            path.reverse()  # TODO check path order
            return path
        for (bstate, bmove, reward) in problem.get_successors():  # alternatively, modify A* to get the successors of currstate+curr+move instead of currstate being prevstate + currmove.
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
    next_moves = a_star_search(problem, node_search_quota=10, heuristic=centerize_alive)
    if next_moves is []:
        return
    return next_moves
