from abc import abstractmethod


class AIBase:
    pass

    def a_star_search(self, board_instance, goal, targs):
        """
        Search the node that has the lowest combined cost and heuristic first.
        """
        queue = [(x, y, z, self.get_mask(x, targs)) for x, y, z in
                 self.get_successors(board_instance)]
        visited = set(x for (x, y, z, w) in queue)
        father = {}
        while len(queue):
            queue.sort(key=lambda x: x[2] + x[3])
            curr_state, curr_move, curr_price, mask = queue.pop(0)
            if curr_state.state[goal[0]][goal[1]] == 0:
                path = []
                while (curr_state, curr_move) in father.keys():
                    path.insert(0, curr_move)
                    curr_state, curr_move = father[(curr_state, curr_move)]
                path.insert(0, curr_move)
                return path
            for (bstate, bmove, cost) in self.get_successors(curr_state):
                if bstate not in visited:
                    queue.append((bstate, bmove, cost + curr_price,
                                  self.get_mask(bstate, targs)))
                    # queue.insert(self.find_loc(g, queue, (bstate, bmove, cost + curr_price)), (bstate, bmove, cost + curr_price))
                    visited.add(bstate)
                    if (bstate, bmove) not in father:
                        father[(bstate, bmove)] = (curr_state, curr_move)
        return []