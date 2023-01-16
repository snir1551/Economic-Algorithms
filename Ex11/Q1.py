import doctest
from typing import List, Dict
from collections import defaultdict
import networkx as nx
from typing import List

def find_trading_cycle(preferences: List[List[int]]):
    """
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
    n = len(preferences)

    vec = []

    for i in range(n):
        if preferences[i][0] == i:
            vec.append(i)
            vec.append(i)
            return vec

    vec.append(0)
    house = preferences[0][0]
    vec.append(house)
    setCycle = set()  # if i reached to cycle
    saveIndex = dict()  # let me the index when the cycle started
    saveIndex.update({0: 0})
    saveIndex.update({house: 1})
    setCycle.add(0)
    setCycle.add(1)
    ansCycle = []
    for i in range(1,n):
        vec.append(preferences[house][0])
        house = preferences[house][0]
        if setCycle.__contains__(house):
            for i in range(saveIndex[house],len(vec)):
                ansCycle.append(vec[i])
        saveIndex.update({house: i})
        setCycle.add(house)

    return ansCycle

def trading_circles_algorithm(preferences: List[List[int]]):
    """
    # >>> preferences = [[1, 2, 0], [2, 1, 0], [1, 2, 0]]
    # >>> trading_circles_algorithm(preferences)
    # ['citizen1 -> home2, citizen2 -> home1', 'citizen0 -> home0']

    >>> preferences = [[2, 1, 0], [2, 1, 0], [2, 1, 0]]
    >>> trading_circles_algorithm(preferences)
    ['citizen2 -> home2', 'citizen1 -> home1', 'citizen0 -> home0']

    >>> preferences = [[0, 1, 2], [0, 2, 1], [0, 1, 2]]
    >>> trading_circles_algorithm(preferences)
    ['citizen0 -> home0', 'citizen1 -> home2, citizen2 -> home1']


    :param preferences:
    :return:
    """
    ans_vec = []
    while len(preferences[0]) > 0:
        vec = find_trading_cycle(preferences)
        ans = ""

        for i in range(len(vec)-1):
            #preferences.remove(preferences[vec[i]-i])
            ans += "citizen" + str(vec[i]) + " -> home" + str(vec[i+1])
            if i < len(vec)-2:
                ans += ", "
        for i in range(len(preferences)):
            for j in range(len(vec)-1):
                preferences[i].remove(vec[j])

        ans_vec.append(ans)

    return ans_vec


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



    # G = find_trading_cycle([[1, 2, 0], [2, 0, 1], [0, 1, 2]])
    # c = nx.find_cycle(G)
    # print(G.edges.data())
    # print(c)