from typing import Tuple

import Game
import math
import Draw
from timeit import default_timer as timer


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


def predict_shoot_heuristic(state: Game, action: Tuple[Tuple[int, int], bool],
                            depth=10):
    return state.predict_projectiles_Score(depth)


def stay_Alive(state: Game, action: Tuple[Tuple[int, int], bool]):
    return state.get_lives() * 1000


def Stay_Alive_Aim_To_Kill(state: Game, action: Tuple[Tuple[int, int], bool]):
    return stay_Alive(state, action) + 100 * predict_shoot_heuristic(state,
                                                                     action,
                                                                     depth=0)


def centerize(state: Game, action: Tuple[Tuple[int, int], bool]):
    return go_to(state, action, (Draw.WIDTH // 2, Draw.LENGTH // 2))


def hunt(state: Game, action: Tuple[Tuple[int, int], bool]):
    for enemy in state.data.EnemySpriteGroup:
        return go_to(state, action, (enemy.location[0] + enemy.imsize[0] // 2,
                                     enemy.location[1] + 100 + enemy.imsize[
                                         1] // 2))
    for enemy in state.data.EnemyBossSpriteGroup:
        return go_to(state, action, (enemy.location[0] + enemy.imsize[0] // 2,
                                     enemy.location[1] + 100 + enemy.imsize[
                                         1] // 2))
    return go_to(state, action, (Draw.WIDTH // 2, Draw.LENGTH // 2))


def hunt_close(state: Game, action: Tuple[Tuple[int, int], bool]):
    player = state.player
    location = [
        player.location[0] + player.imsize[0] // 2,
        player.location[1] + player.imsize[1] // 2]
    closest_enemy = None
    min = 10000000
    for enemy_boss in state.data.EnemyBossSpriteGroup:
        return go_to(state, action, (enemy_boss.location[0] + enemy_boss.imsize[0] // 2,
                                     enemy_boss.location[1] + 100 + enemy_boss.imsize[
                                         1] // 2))
    for enemy in state.data.EnemySpriteGroup:
        dis = distance(location, (enemy.location[0] + enemy.imsize[0] // 2,
                                  enemy.location[1] + 100 + enemy.imsize[
                                      1] // 2))
        if min > dis:
            min = dis
            closest_enemy = enemy
    if closest_enemy is not None:
        return go_to(state, action, (
        closest_enemy.location[0] + closest_enemy.imsize[0] // 2,
        closest_enemy.location[1] + 100 + closest_enemy.imsize[1] // 2))
    return hunt(state, action)

def go_to(state: Game, action: Tuple[Tuple[int, int], bool], destination):
    player = state.player
    location = [player.location[0] + player.imsize[0] // 2,
                player.location[1] + player.imsize[1] // 2]
    dis = - 30 * distance(location, destination)
    return dis


def hunt_alive(state: Game, action: Tuple[Tuple[int, int], bool]):
    return stay_Alive(state, action) + hunt(state, action)


def hunt_alive_close(state: Game, action: Tuple[Tuple[int, int], bool]):
    return stay_Alive(state, action) + hunt_close(state, action)


def distance_2d(point1, point2):
    return math.pow(point2[0] - point1[0], 2)


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
        mval = func(arr[m])  # TODO store the heuristic return value -_-
        if mval > element_val:
            l = m + 1
        else:
            h = m
    return l

def find_loc_mem():
    values = dict()
    def find_loc(func, arr, element):
        l = 0
        h = len(arr)
        values[element[0]] = func(element)
        element_val = values[element[0]]
        while h > l:
            m = (h + l) // 2
            if arr[m][0] not in values:
                values[arr[m][0]] = func(arr[m])
            mval = values[arr[m][0]]
            if mval > element_val:
                l = m + 1
            else:
                h = m
        return l
    return find_loc

def a_star_search_times(problem: Game, time_per_frame,
                        heuristic=hunt_alive_close, largest_path = 30):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    queue = problem.get_successors()
    visited = set(x for (x, y, z) in queue)
    path = {}
    find_local = find_loc_mem()
    for state, move, score in queue:
        path[state] = [(state, move, score)]
    g = lambda x: x[2] + heuristic(x[0], x[1])
    def search():
        nonlocal queue
        start = timer()
        while len(queue):
            curr_state, curr_move, score = queue.pop(0)
            if timer() - start > time_per_frame or len(path[curr_state]) > largest_path:
                chosen = path[curr_state][0]
                del path[chosen[0]]
                new_queue = []
                for key in path.keys():
                    if path[key][0] == chosen:
                        path[key].pop(0)
                        new_queue.append(path[key][-1])
                if len(new_queue) == 0:
                    new_queue = curr_state.get_successors()
                    for state, move, score in new_queue:
                        path[state] = [(state, move, score)]
                queue = new_queue
                print(len(queue))
                return chosen[1]
            if len(path[curr_state]) == 10:
                continue
            for (bstate, bmove, reward) in curr_state.get_successors():
                if bstate not in visited:
                    queue_elem = (bstate, bmove, reward + score)
                    queue.insert(find_local(g, queue, queue_elem), queue_elem)
                    visited.add(bstate)
                    path[bstate] = path[curr_state] + [queue_elem]
        return ([0, 0], False)
    return search


def a_star_search(problem: Game, node_search_quota=10000,
                  heuristic=null_heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    queue = problem.get_successors()
    visited = set(x for (x, y, z) in queue)
    father = {}
    g = lambda x: x[2] + heuristic(x[0], x[
        1])  # x = (curr_state, curr_move, score), where the current state is the state *after* curr_move has been executed, and the score is also after the move.
    i = 0
    while len(queue):
        curr_state, curr_move, score = queue.pop(
            0)  # reversed from min to max (score)
        # print(len(queue), [i for i in range(len(queue)) if queue[i][1][0] == [0, 0]])
        if node_search_quota == i:
            path = []
            key = get_key(curr_state, curr_move)
            while key in father.keys():
                path.insert(0, curr_move)
                curr_state, curr_move = father[key]
                key = get_key(curr_state, curr_move)
            path.insert(0, curr_move)
            return path
        for (bstate, bmove,
             reward) in curr_state.get_successors():  # alternatively, modify A* to get the successors of currstate+curr+move instead of currstate being prevstate + currmove.
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


def a_star_player(problem: Game, expanded_node_count=10):
    next_moves = a_star_search(problem, node_search_quota=expanded_node_count,
                               heuristic=hunt_alive)
    if next_moves is []:
        return
    return next_moves

