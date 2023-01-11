import math

import networkx as nx
from networkx import NetworkXUnbounded, NetworkXError


def build_digraph_logarithm(mat):
    """
    >>> mat1 = [[0, 0.38, 0.0, 0], [0.38, 0, 1.0, 0], [0.0, 1.0, 0, 2], [0.0, 0, 2, 0]]
    >>> print(build_digraph_logarithm(mat1).edges.data())
    [(0, 1, {'weight': -1.3959286763311392}), (1, 0, {'weight': -1.3959286763311392}), (1, 2, {'weight': 0.0}), (2, 1, {'weight': 0.0}), (2, 3, {'weight': 1.0}), (3, 2, {'weight': 1.0})]

    >>> mat2 = [[0, 2, 0, 0],[0, 0, 3, 0],[0, 0, 0, 4],[1, 0, 0, 0]]
    >>> print(build_digraph_logarithm(mat2).edges.data())
    [(0, 1, {'weight': 1.0}), (1, 2, {'weight': 1.5849625007211563}), (2, 3, {'weight': 2.0}), (3, 0, {'weight': 0.0})]

    >>> mat3 = [[0, 2, 0, 0],[0, 0, 0.38, 0],[0, 0, 0, 1],[0, 1, 0, 0]]
    >>> print(build_digraph_logarithm(mat3).edges.data())
    [(0, 1, {'weight': 1.0}), (1, 2, {'weight': -1.3959286763311392}), (2, 3, {'weight': 0.0}), (3, 1, {'weight': 0.0})]


    :param mat:
    :return:
    """

    G = nx.DiGraph()
    for i in range(len(mat)):
        G.add_node(i)

    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j or mat[i][j] == 0:
                continue
            logarithm_number = math.log(mat[i][j], 2)
            G.add_weighted_edges_from([(i, j, logarithm_number)])
            # print((i,j,logarithm_number))
    return G


def find_cycle(mat, start):
    """
    >>> mat1 = [[0, 0.38, 0.0, 0], [0.38, 0, 1.0, 0], [0.0, 1.0, 0, 2], [0.0, 0, 2, 0]]
    >>> print(find_cycle(mat1,0))
    [0, 1, 0]
    >>> mat2 = [[0, 2, 0, 0],[0, 0, 3, 0],[0, 0, 0, 4],[1, 0, 0, 0]]
    >>> print(find_cycle(mat2,0))
    None
    >>> mat3 = [[0, 2, 0, 0],[0, 0, 0.38, 0],[0, 0, 0, 1],[0, 1, 0, 0]]
    >>> print(find_cycle(mat3,0))
    [3, 1, 2, 3]

    >>> mat3 = [[0, 2, 0, 0],[0, 0, 0.38, 0],[0, 0, 0, 1],[0, 1, 0, 0]]
    >>> print(find_cycle(mat3,0))
    [3, 1, 2, 3]

    >>> mat3 = [[0, 2, 0, 0],[0, 0, 0.38, 0],[0, 0, 0, 1],[0, 0, 0, 0]]
    >>> print(find_cycle(mat3,0))
    None

    :param mat:
    :param start:
    :return:
    """
    digraph = build_digraph_logarithm(mat)
    try:
        cycle = nx.find_negative_cycle(digraph, start)
        return cycle
    except NetworkXError:
        return "None"


# def logarithm_of_edge(G):

if __name__ == '__main__':
    import doctest

    doctest.testmod()

