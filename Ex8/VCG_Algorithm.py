from typing import List
import doctest
import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict


class Agent:
    def __init__(self, name):
        self.name = name
        self.options: Dict[str, float] = dict()

    def set_option(self, option: str, value: float):  # add option
        self.options.update({option: value})

    def value(self, option: str) -> float:  # return value of option
        if self.options.get(option) is None:  # option doesn't exist
            return -1
        return self.options[option]


def VCG_Algorithm(agents: List[Agent]):
    """
     >>> AmiAgent = Agent('Ami')
     >>> AmiAgent.set_option('item1', 8)
     >>> AmiAgent.set_option('item2', 4)

     >>> TamiAgent = Agent('Tami')
     >>> TamiAgent.set_option('item1', 5)
     >>> TamiAgent.set_option('item2', 8)

     >>> e = [AmiAgent, TamiAgent]

    >>> VCG_Algorithm(e)
    max_option: = 16
    max without:  Ami : 8
    Ami pay:  8 - 8 = 0
    max without:  Tami : 8
    Tami pay:  8 - 8 = 0


    >>> AmiAgent1 = Agent('Ami')
    >>> AmiAgent1.set_option('item1', 8)
    >>> AmiAgent1.set_option('item2', 4)
    >>> AmiAgent1.set_option('item3', 3)

    >>> TamiAgent1 = Agent('Tami')
    >>> TamiAgent1.set_option('item1', 5)
    >>> TamiAgent1.set_option('item2', 8)
    >>> TamiAgent1.set_option('item3', 1)

    >>> RamiAgent1 = Agent('Rami')
    >>> RamiAgent1.set_option('item1', 3)
    >>> RamiAgent1.set_option('item2', 5)
    >>> RamiAgent1.set_option('item3', 3)

    >>> f = [AmiAgent1, TamiAgent1, RamiAgent1]

    >>> VCG_Algorithm(f)
    max_option: = 19
    max without:  Ami : 11
    Ami pay:  11 - 11 = 0
    max without:  Tami : 13
    Tami pay:  13 - 11 = 2
    max without:  Rami : 16
    Rami pay:  16 - 16 = 0


    >>> AmiAgent2 = Agent('Ami')
    >>> AmiAgent2.set_option('item1', 1)
    >>> AmiAgent2.set_option('item2', 2)
    >>> AmiAgent2.set_option('item3', 3)
    >>> AmiAgent2.set_option('item4', 4)
    >>> AmiAgent2.set_option('item5', 11)

    >>> TamiAgent2 = Agent('Tami')
    >>> TamiAgent2.set_option('item1', 1)
    >>> TamiAgent2.set_option('item2', 2)
    >>> TamiAgent2.set_option('item3', 3)
    >>> TamiAgent2.set_option('item4', 4)
    >>> TamiAgent2.set_option('item5', 8)

    >>> RamiAgent2 = Agent('Rami')
    >>> RamiAgent2.set_option('item1', 1)
    >>> RamiAgent2.set_option('item2', 2)
    >>> RamiAgent2.set_option('item3', 3)
    >>> RamiAgent2.set_option('item4', 4)
    >>> RamiAgent2.set_option('item5', 9)



    >>> g = [AmiAgent2, TamiAgent2, RamiAgent2]

    >>> VCG_Algorithm(g)
    max_option: = 18
    max without:  Ami : 13
    Ami pay:  13 - 7 = 6
    max without:  Tami : 15
    Tami pay:  15 - 15 = 0
    max without:  Rami : 15
    Rami pay:  15 - 14 = 1

    :param agents:
    :return:
    """
    G = build_bilateral_graph(agents)  # create bilateral_graph
    maximum, max_weight_matching_with_player = max_weight_matching_algorithm(G)
    print("max_option:", "=", maximum)
    # print(max_weight_matching_with_player)
    G1 = G.copy()  # copy graph
    for agent in agents:
        G1.remove_node(agent.name)  # remove node (and his edges)
        max_without_player, w = max_weight_matching_algorithm(
            G1)  # finding the placement that maximizes the sum of values
        print("max without: ", agent.name, ":", max_without_player)
        # print(w)
        max_option = maximum - get_value_player(G, max_weight_matching_with_player,
                                                agent.name)  # the maximum with the player - his value
        print(agent.name, "pay: ", max_without_player, "-", max_option, "=",
              max_without_player - (maximum - get_value_player(G, max_weight_matching_with_player, agent.name)))
        # print("Maximum-value matching: ", nx.max_weight_matching(G1))
        G1 = G.copy()  # back node (and his edges)


def max_weight_matching_algorithm(G):
    max = 0
    max_weight_matching = nx.max_weight_matching(G)
    for node1, node2 in max_weight_matching:
        max += G[node1][node2]["weight"]

    return max, max_weight_matching


def get_value_player(G, max_weight_matching, option):
    # print(max_weight_matching)
    value = 0
    for node1, node2 in max_weight_matching:
        if node1 == option or node2 == option:
            value = G[node1][node2]["weight"]
            break

    return value


def build_bilateral_graph(agents: List[Agent]):
    G = nx.Graph()
    for i in agents:
        for j in i.options.keys():
            G.add_edge(i.name, j, weight=i.value(j))

    return G


def draw_graph(G, pos):
    plt.figure()

    nx.draw(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    """
    AmiAgent3 = Agent('Ami')
    AmiAgent3.set_option('item1', 8)
    AmiAgent3.set_option('item2', 4)

    TamiAgent3 = Agent('Tami')
    TamiAgent3.set_option('item1', 5)
    TamiAgent3.set_option('item2', 8)

    e = [AmiAgent3, TamiAgent3]
    pos = {'Ami': (0, 0), 'Tami': (0, 0.3), 'item1': (3, 0.0), 'item2': (3, 0.8)}
    G = build_bilateral_graph(e)
    draw_graph(G,pos)
    """
