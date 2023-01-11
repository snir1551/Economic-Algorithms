from typing import Dict
from typing import List


class Agent:
    def __init__(self):
        self.options: Dict[int, float] = dict()

    def set_option(self, option: int, value: float):  # add option
        self.options.update({option: value})

    def value(self, option: int) -> float:  # return value of option
        if self.options.get(option) is None:  # option doesn't exist
            return -1
        return self.options[option]


def isParetoImprovement(agents: List[Agent], option1: int, option2: int) -> bool:
    count_equal_value = 0  # counter of equal values in option 1 to option 2
    if option1 == option2:
        return False
    for x_agent in agents:
        if x_agent.value(option1) < x_agent.value(option2):
            return False
        elif x_agent.value(option1) == x_agent.value(option2):
            count_equal_value += 1

    if count_equal_value == len(agents):
        return False
    else:
        return True


def isParetoOptimal(agents: List[Agent], option: int, allOptions: List[int]) -> bool:
    for option_another_agent in allOptions:
        if option == option_another_agent:
            continue
        if isParetoImprovement(agents, option_another_agent, option):
            return False

    return True
