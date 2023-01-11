import agent

"""
    [A,B,C,D,E]
 Ami[1,2,3,4,5]
Tami[3,1,2,5,4]
Rami[3,5,5,1,1]
"""


def first_example():
    AmiAgent = agent.Agent()
    AmiAgent.set_option(1, 1)
    AmiAgent.set_option(2, 2)
    AmiAgent.set_option(3, 3)
    AmiAgent.set_option(4, 4)
    AmiAgent.set_option(5, 5)

    TamiAgent = agent.Agent()
    TamiAgent.set_option(1, 3)
    TamiAgent.set_option(2, 1)
    TamiAgent.set_option(3, 2)
    TamiAgent.set_option(4, 5)
    TamiAgent.set_option(5, 4)

    RamiAgent = agent.Agent()
    RamiAgent.set_option(1, 3)
    RamiAgent.set_option(2, 5)
    RamiAgent.set_option(3, 5)
    RamiAgent.set_option(4, 1)
    RamiAgent.set_option(5, 1)

    return [AmiAgent, TamiAgent, RamiAgent]


"""
    [A,B,C,D]
 Ami[2,0,0,2]
Tami[1,1,1,1]

"""


def second_example():
    AmiAgent = agent.Agent()
    AmiAgent.set_option(1, 2)
    AmiAgent.set_option(2, 0)
    AmiAgent.set_option(3, 0)
    AmiAgent.set_option(4, 2)

    TamiAgent = agent.Agent()
    TamiAgent.set_option(1, 1)
    TamiAgent.set_option(2, 1)
    TamiAgent.set_option(3, 1)
    TamiAgent.set_option(4, 1)

    return [AmiAgent, TamiAgent]


"""
    [A,B]
 Ami[1,3]
Tami[2,2]
Rami[3,1]

"""


def third_example():
    AmiAgent = agent.Agent()
    AmiAgent.set_option(1, 1)
    AmiAgent.set_option(2, 3)

    TamiAgent = agent.Agent()
    TamiAgent.set_option(1, 2)
    TamiAgent.set_option(2, 2)

    RamiAgent = agent.Agent()
    RamiAgent.set_option(1, 3)
    RamiAgent.set_option(2, 1)

    return [AmiAgent, TamiAgent, RamiAgent]


"""
    [A,B,C]
 Ami[1,3,3]
Tami[2,2,3]
Rami[3,1,3]

"""


def fourth_example():
    AmiAgent = agent.Agent()
    AmiAgent.set_option(1, 1)
    AmiAgent.set_option(2, 3)
    AmiAgent.set_option(3, 3)

    TamiAgent = agent.Agent()
    TamiAgent.set_option(1, 2)
    TamiAgent.set_option(2, 2)
    TamiAgent.set_option(3, 3)

    RamiAgent = agent.Agent()
    RamiAgent.set_option(1, 3)
    RamiAgent.set_option(2, 1)
    RamiAgent.set_option(3, 3)

    return [AmiAgent, TamiAgent, RamiAgent]


if __name__ == '__main__':
    """
        [A,B,C,D,E]
    Tami[1,2,3,4,5]
     Ami[3,1,2,5,4]
    Rami[3,5,5,1,1]
    """
    list1 = first_example()
    list2 = [1, 2, 3, 4, 5]
    print("----------checking isParetoImprovement----------")
    result = agent.isParetoImprovement(list1, 7, 1)  # not exist option
    print(result)  # -> false
    result = agent.isParetoImprovement(list1, 1, 1)  # equal option
    print(result)  # -> false
    result = agent.isParetoImprovement(list1, 1, 2)  # Option 1 is not an improvement of option 2 (1 < 2)
    print(result)  # -> false
    result = agent.isParetoImprovement(list1, 1, 3)  # Option 1 is not an improvement of option 3 (1 < 3)
    print(result)  # -> false
    result = agent.isParetoImprovement(list1, 1, 4)  # Option 1 is not an improvement of option 4 (1 < 4)
    print(result)  # -> false
    result = agent.isParetoImprovement(list1, 2, 1)  # Option 2 is not an improvement of option 5 (1 < 3)
    print(result)  # -> false
    result = agent.isParetoImprovement(list1, 2, 3)  # Option 2 is not an improvement of option 3 (2 < 3)
    print(result)  # -> false
    result = agent.isParetoImprovement(list1, 2, 4)  # Option 2 is not an improvement of option 4 (2 < 4)
    print(result)  # -> false
    result = agent.isParetoImprovement(list1, 2, 5)  # Option 2 is not an improvement of option 5 (2 < 5)
    print(result)  # -> false

    result = agent.isParetoImprovement(list1, 3, 2)  # Option 3 is an improvement of option 2 (3 > 2, 2 > 1, 5=5)
    print(result)  # -> true

    print("----------checking isParetoOptimal----------")

    result1 = agent.isParetoOptimal(list1, 1, list2)  # pareto efficient
    print(result1)  # true
    result1 = agent.isParetoOptimal(list1, 2, list2)  # Option 3 is an improvement of option 2 -> not pareto efficient
    print(result1)  # false
    result1 = agent.isParetoOptimal(list1, 3, list2)  # pareto efficient
    print(result1)  # true
    result1 = agent.isParetoOptimal(list1, 4, list2)  # pareto efficient
    print(result1)  # true
    result1 = agent.isParetoOptimal(list1, 5, list2)  # pareto efficient
    print(result1)  # true

    print("*****************Example 2*****************")

    """
        [A,B,C,D]
     Ami[2,0,0,2]
    Tami[1,1,1,1]

    """
    list1 = second_example()
    list2 = [1, 2, 3, 4]

    print("----------checking isParetoImprovement----------")
    result = agent.isParetoImprovement(list1, 3, 2)  # Option 3 is not an improvement of option 2 (0=0, 1=1)
    print(result)  # false

    print("----------checking isParetoOptimal----------")
    result1 = agent.isParetoOptimal(list1, 1, list2)
    print(result1)  # true

    print("*****************Example 3*****************")

    """
        [A,B]
     Ami[1,3]
    Tami[2,2]
    Rami[3,1]

    """

    list1 = third_example()
    list2 = [1, 2]
    print("----------checking isParetoImprovement----------")
    result1 = agent.isParetoImprovement(list1, 1, 2)  # Option 1 is not an improvement of option 2 (1 < 3)
    print(result1)  # false
    result1 = agent.isParetoImprovement(list1, 2, 1)  # Option 2 is not an improvement of option 1 (3 > 1)
    print(result1)  # false

    print("----------checking isParetoOptimal----------")
    result1 = agent.isParetoOptimal(list1, 1, list2)
    print(result1)  # true

    result1 = agent.isParetoOptimal(list1, 2, list2)
    print(result1)  # true

    print("*****************Example 4*****************")

    """
        [A,B,C]
     Ami[1,3,3]
    Tami[2,2,3]
    Rami[3,1,3]

    """

    list1 = fourth_example()
    list2 = [1, 2, 3]

    print("----------checking isParetoOptimal----------")
    result1 = agent.isParetoOptimal(list1, 3, list2)
    print(result1)  # true
    result1 = agent.isParetoOptimal(list1, 2, list2)
    print(result1)  # false
    result1 = agent.isParetoOptimal(list1, 1, list2)
    print(result1)  # false
