import doctest
from typing import List, Dict
from collections import defaultdict
import networkx as nx
from typing import List
from collections import deque
import matplotlib.pyplot as plt
import re

def find_trading_cycle(preferences: List[List[int]]):
    """

    Finds a trading cycle given a list of preferences.
    A trading cycle is a sequence of citizens and homes such that each citizen is matched to their
    most preferred home, and each home is matched to its most preferred citizen.

    :param preferences: A list of lists, where each list represents the preferences of a citizen.
                      The first element of each list is the most preferred home, the second is the
                      second most preferred, and so on.
    :return: A list representing the trading cycle, where the first element is the starting point
             of the cycle, and the last element is the starting point.

     Examples:

    >>> preferences = [[1, 2, 0], [2, 0, 1], [0, 1, 2]]
    >>> find_trading_cycle(preferences)
    [0, 1, 2, 0]
    >>> preferences = [[2, 1, 0], [2, 0, 1], [0, 1, 2]]
    >>> find_trading_cycle(preferences)
    [0, 2, 0]
    >>> preferences = [[0, 1, 2], [1, 0, 2], [2, 1, 0]]
    >>> find_trading_cycle(preferences)
    [0, 0]
    >>> preferences = [[2, 1, 0], [2, 1, 0], [2, 1, 0]]
    >>> find_trading_cycle(preferences)
    [2, 2]
    >>> preferences = [[1, 2, 0], [2, 1, 0], [1, 2, 0]]
    >>> find_trading_cycle(preferences)
    [1, 2, 1]

    :param preferences:
    :return:
    """
    # Get the number of citizens
    n = len(preferences)
    # Create a set to keep track of matched citizens
    matched_citizens = set()
    # Create a deque to store the trading cycle
    trading_cycle = deque()
    # Start the algorithm with the first citizen
    current_citizen = 0

    # Repeat until a citizen is matched to their own home
    while current_citizen not in matched_citizens:
        # Add the current citizen to the set of matched citizens
        matched_citizens.add(current_citizen)
        # Add the current citizen to the trading cycle
        trading_cycle.append(current_citizen)
        # Get the next citizen in the cycle
        current_citizen = preferences[current_citizen][0]

    # Find the starting point of the cycle
    cycle_start = trading_cycle.index(current_citizen)
    # Convert the deque to a list and slice it to get the cycle
    trading_cycle = list(trading_cycle)[cycle_start:]
    # Add the starting point of the cycle to the result
    trading_cycle.append(trading_cycle[0])
    # Return the final trading cycle
    return trading_cycle

def trading_circles_algorithm(preferences: List[List[int]]):
    """

    >>> preferences = [[1, 2, 0], [2, 1, 0], [1, 2, 0]]
    >>> trading_circles_algorithm(preferences)
    ['citizen1 -> home2, citizen2 -> home1', 'citizen0 -> home0']
    >>> preferences = [[2, 1, 0], [2, 1, 0], [2, 1, 0]]
    >>> trading_circles_algorithm(preferences)
    ['citizen2 -> home2', 'citizen1 -> home1', 'citizen0 -> home0']
    >>> preferences = [[0, 1, 2], [0, 2, 1], [0, 1, 2]]
    >>> trading_circles_algorithm(preferences)
    ['citizen0 -> home0', 'citizen1 -> home2, citizen2 -> home1']

    >>> preferences = [[3, 7, 1, 5, 6, 4, 2, 0], [1, 0, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1, 0], [1, 2, 3, 4, 5, 6, 7, 0], [3, 2, 1, 0, 4, 5, 6, 7], [6, 5, 4, 3, 2, 1, 0, 7], [4, 3, 2, 1, 0, 5, 6, 7], [5, 4, 3, 2, 1, 0, 7, 6]]
    >>> trading_circles_algorithm(preferences)
    ['citizen1 -> home1', 'citizen3 -> home2, citizen2 -> home7, citizen7 -> home5, citizen5 -> home6, citizen6 -> home4, citizen4 -> home3', 'citizen0 -> home0']

    """
    # Create an empty list to store the final trading cycles
    ans_vec = []
    # Create a set to keep track of matched citizens
    matched_citizens = set()
    # Create a set to keep track of matched homes
    matched_homes = set()
    # While all citizens haven't been matched
    while len(matched_citizens) < len(preferences):
        # Find the next trading cycle
        vec = find_trading_cycle(preferences)
        ans = ""
        # Iterate through the trading cycle
        for i in range(len(vec) - 1):
            current_citizen = vec[i]
            current_home = vec[i + 1]
            # Construct the string for the current trading cycle
            ans += "citizen{} -> home{}".format(current_citizen, current_home)
            # Add the current citizen and home to the matched sets
            matched_citizens.add(current_citizen)
            matched_homes.add(current_home)
            # Add a separator if it's not the last element
            if i < len(vec) - 2:
                ans += ", "
        # Add the current trading cycle to the final list
        ans_vec.append(ans)
        # Remove the matched citizens and homes from the preferences list
        for i in range(len(preferences)):
            for j in range(len(vec) - 1):
                if vec[j] in matched_citizens and vec[j + 1] in matched_homes:
                    preferences[i].remove(vec[j])
    return ans_vec


def visualize_matchings(matchings: List[str]) -> None:
    """

    :param matchings:
    :return:
    """
    citizens = []
    homes = []
    for match in matchings:
        citizen_home = re.findall(r'\d+', match)
        citizens = [citizen_home[i] for i in range(0, len(citizen_home), 2)]
        homes = [citizen_home[i] for i in range(1, len(citizen_home), 2)]
        plt.scatter(citizens, homes)

    plt.xlabel("Citizens")
    plt.ylabel("Homes")
    plt.show()


def test_visualize_matchings():
    matchings = ['citizen1 -> home2, citizen2 -> home1', 'citizen0 -> home0']
    visualize_matchings(matchings)
    assert True
    matchings = trading_circles_algorithm([[3, 7, 1, 5, 6, 4, 2, 0], [1, 0, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1, 0], [1, 2, 3, 4, 5, 6, 7, 0], [3, 2, 1, 0, 4, 5, 6, 7], [6, 5, 4, 3, 2, 1, 0, 7], [4, 3, 2, 1, 0, 5, 6, 7], [5, 4, 3, 2, 1, 0, 7, 6]])
    visualize_matchings(matchings)
    assert True



# def find_trading_cycle(preferences: List[List[int]]):
#     """
#         >>> preferences = [[1, 2, 0], [2, 0, 1], [0, 1, 2]]
#         >>> find_trading_cycle(preferences)
#         ['0', '1', '0']
#         >>> preferences = [[0, 1], [1,0]]
#         >>> find_trading_cycle(preferences)
#         ['0', '1', '0']
#
#         >>> preferences = [[2,1,3], [2,1,3], [4,1,2]]
#         >>> find_trading_cycle(preferences)
#         """
#
#     G = nx.DiGraph()
#     for i in range(len(preferences)):
#         citizen = "citizen" + str(i)
#         homeCitizen = "home" + str(i)
#         G.add_node(citizen)
#         G.add_node(homeCitizen)
#         G.add_edge(citizen,homeCitizen,weight=preferences[i][i])
#     max1 = -1
#     index_of_max = 0
#     for i in range(len(preferences)):
#        #print(preferences[i].index(max(preferences[i])))
#        for j in range(len(preferences[0])):
#            if max1 < preferences[i][j]:
#                max1 = preferences[i][j]
#                index_of_max = j
#        citizen = "citizen" + str(i)
#        homeCitizen = "home" + str(index_of_max)
#        max1 = -1
#        G.add_edge(homeCitizen, citizen, weight=preferences[i][i])
#
#     c = nx.find_cycle(G)
#     vec = []
#     #print(c[0][1])
#     #print(c[0][0])
#     last_element_in_cycle = len(c)-2
#     vec.append(c[0][0][-1])
#     vec.append(c[last_element_in_cycle+1][0][-1])
#     vec.append(c[0][1][-1])
#
#     return vec








if __name__ == '__main__':
    import doctest

    doctest.testmod()

    test_visualize_matchings()
