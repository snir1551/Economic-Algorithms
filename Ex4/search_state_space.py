import math
import queue
from typing import Dict
import json


def state_space_search_BFS(matrix: list[list]) -> dict:
    q_fifo = queue.Queue()  # FIFO
    q_fifo.put([0] * len(matrix[0]))  # add to stack array with zero values
    count_states_deleted = 0  # number of states that deleted
    visit = set()  # for check if we visited
    visit.add((0, 0, 0))
    index_object = 0  # index of object
    tree: Dict[int, list] = dict()  # dictionary that will contain the all combinations
    min_between_players = math.inf
    max_between_objects = 0
    next_object = 0
    # ans.update({i: [0, 0, 0]})
    num_current_rank = math.pow(len(matrix[0]), index_object)
    while not q_fifo.empty():  # while the queue is not empty
        # print(stack.pop())
        a = q_fifo.get()  # pop the vector from the queue
        # print(a)
        for index_player in range(len(matrix[0])):  # goes over all players in the vector
            a[index_player] += matrix[index_object][
                index_player]  # summarize what the player currently has and what he should have at the next level
            if visit.__contains__(tuple(a)):  # check if visited
                a[index_player] -= matrix[index_object][index_player]
                for i in range(len(matrix) - index_object):  # Calculate how many states we actually deleted
                    count_states_deleted += math.pow(len(matrix[0]), i)
                print("count_states")
                print(count_states_deleted)
                continue  # if visited -> continue
            visit.add(tuple(a))  # if not visited add him to visit.
            if tree.get(index_object) is None:  # if not exists key in the dictionary of tree
                tree.update({index_object: [a.copy()]})  # update dictionary

            else:
                tree.get(index_object).append(a.copy())  # if exists key, so append to dictionary

            # print(a)
            if len(matrix) - 1 > index_object:  # If it's not the last level
                #print(len(matrix) - 1)
                q_fifo.put(a.copy())
            else:  # If this is the last level
                for player_value in range(len(matrix[0])):  # find the minimum among the players
                    if min_between_players > a[player_value]:
                        min_between_players = a[player_value]

                if max_between_objects < min_between_players:  # update the egalitarian value
                    max_between_objects = min_between_players
                min_between_players = math.inf  # back minimum to infinite (for check the new minimum of the other object)

            a[index_player] -= matrix[index_object][index_player]
        num_current_rank -= 1
        if num_current_rank == 0:  # Checks if the current rank is finished
            index_object += 1  # next object
            num_current_rank = math.pow(len(matrix[0]), index_object)
            print("-----------------")
            print(tree)
            print("-----------------")

    return max_between_objects


def draw_tree(tree: dict):
    pretty = json.dumps(tree, indent=4, sort_keys=True)
    print(pretty)
