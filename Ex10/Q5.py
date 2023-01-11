import itertools
import math
from typing import List
import doctest
import numpy as np
from itertools import combinations


def compute_budget(total_budget: float, citizen_votes: List[List]) -> List[float]:
    """
    >>> citizen_votes1 = [[6, 0, 6], [6, 0, 6], [6, 6, 0], [6,6,0],[0,6,6],[0,6,6], [6,0,0], [0,6,0], [0,0,6]]
    >>> total_budget1 = 30
    >>> compute_budget(total_budget1,citizen_votes1)
    [0.06666666667, [1.9999999999998863, 3.9999999999997726], [3.9999999999997726, 3.9999999999997726, 3.9999999999997726, 3.9999999999997726, 3.9999999999997726, 3.9999999999997726, 1.9999999999998863, 1.9999999999998863, 1.9999999999998863], 30.0]

    >>> citizen_votes2 = [[30, 0, 0], [0, 15, 15], [0, 15, 15]]
    >>> total_budget2 = 30
    >>> compute_budget(total_budget2,citizen_votes2)
    [0.2, [5.999999999999659, 11.999999999999318], [5.999999999999659, 11.999999999999318, 11.999999999999318], 30.0]

    :param total_budget:
    :param citizen_votes:
    :return:
    """

    c_b = binary_search(citizen_votes, 0, 1, total_budget, 1)
    return c_b


def c_votes(cizizen_votes_size: int, t: float, c: float):
    """
        >>> cizizen_votes_size1 = 3
        >>> t1 = 1/15
        >>> c1 = 30
        >>> c_votes(cizizen_votes_size1, t1, c1)
        [2.0, 4.0]

        >>> cizizen_votes_size2 = 3
        >>> t2 = 0.2
        >>> c2 = 30
        >>> c_votes(cizizen_votes_size2, t2, c2)
        [6.0, 12.0]

        >>> cizizen_votes_size1 = 4
        >>> t1 = 1/15
        >>> c1 = 30
        >>> c_votes(cizizen_votes_size1, t1, c1)
        [2.0, 4.0, 6.0]

        >>> cizizen_votes_size1 = 5
        >>> t1 = 1/15
        >>> c1 = 30
        >>> c_votes(cizizen_votes_size1, t1, c1)
        [2.0, 4.0, 6.0, 8.0]

        :param cizizen_votes_size:
        :param t:
        :param c:
        :return:
    """

    const_votes = []

    for i in range(1, cizizen_votes_size):
        const_votes.append(c * min(1, i * t))
    return const_votes


def find_medians(citizen_votes: List[List], const_votes: list):
    """
    >>> citizen_votes1 = [[30, 0, 0], [0, 15, 15], [0, 15, 15]]
    >>> const_votes1 = [6, 12]
    >>> find_medians(citizen_votes1, const_votes1)
    [6, 12, 12]

    >>> citizen_votes2 = [[30, 0, 0], [0, 15, 15], [0, 15, 15]]
    >>> const_votes2 = [5.625, 11.25]
    >>> find_medians(citizen_votes2, const_votes2)
    [5.625, 11.25, 11.25]

    >>> citizen_votes3 = [[6, 0, 6], [6, 0, 6], [6, 6, 0], [6,6,0],[0,6,6],[0,6,6], [6,0,0], [0,6,0], [0,0,6]]
    >>> const_votes3 = [2,4]
    >>> find_medians(citizen_votes3, const_votes3)
    [4, 4, 4, 4, 4, 4, 2, 2, 2]

    >>> citizen_votes4 = [[30, 0, 0,2], [0, 15, 15,2], [0, 15, 15,2]]
    >>> const_votes4 = [6, 12]
    >>> find_medians(citizen_votes4, const_votes4)
    [4.0, 9.0, 9.0]

    >>> citizen_votes4 = [[30, 30,30,30,0,0,0,0,0,0], [0, 0,0,0,30,30,30,0,0,0], [0,0,0,0,0,0,0,30,30,30]]
    >>> const_votes4 = [15.0, 30]
    >>> find_medians(citizen_votes4, const_votes4)
    [7.5, 0.0, 0.0]

    >>> citizen_votes4 = [[1,2,3,4,5,6,7]]
    >>> const_votes4 = [8,9,10,11,12,13]
    >>> find_medians(citizen_votes4, const_votes4)
    [7]

    :param citizen_votes:
    :param const_votes:
    :return:
    """
    sorted_citizen_votes = []
    for i in citizen_votes:
        sorted_citizen_votes.append(i.copy())
    for i in range(len(sorted_citizen_votes)):
        sorted_citizen_votes[i] += const_votes
    sorted_citizen_votes = sort_citizen_votes(sorted_citizen_votes)
    medians = []
    for i in sorted_citizen_votes:
        if len(i) % 2 == 0:
            medians.append((i[(len(i) - 1) // 2] + i[(len(i) // 2)]) / 2)
        else:
            medians.append(i[(len(i) - 1) // 2])

    return medians


def sum_medians(medians: List):
    """
        >>> medians1 = [6,12,12]
        >>> sum_medians(medians1)
        30

        >>> medians2 = [4,4,4,4,4,4,2,2,2]
        >>> sum_medians(medians2)
        30

        :param medians:
        :return:
    """
    return sum(medians)


def sort_citizen_votes(citizen_votes: List[List]):
    """
        >>> citizen_votes1 = [[30,15,2,0,40], [1,3,7,0,90], [5,4,3,2,1]]
        >>> sort_citizen_votes(citizen_votes1)
        [[0, 2, 15, 30, 40], [0, 1, 3, 7, 90], [1, 2, 3, 4, 5]]


        :param citizen_votes:
        :return:
    """
    ans = []
    sorted_citizen_votes = citizen_votes.copy()
    for i in sorted_citizen_votes:
        ans.append(sorted(i))
    return ans


def binary_search(citizen_votes: List[List], low, high, total_budget: float, i):
    """
        >>> citizen_votes1 = [[30, 0, 0], [0, 15, 15], [0, 15, 15]]
        >>> const_votes1 = [6, 12]
        >>> total_budget1 = 30
        >>> binary_search(citizen_votes1,0,1,total_budget1,0)
        [0.2, [5.999999999999659, 11.999999999999318], [5.999999999999659, 11.999999999999318, 11.999999999999318], 30.0]
        >>> citizen_votes2 = [[6, 0, 6], [6, 0, 6], [6, 6, 0], [6,6,0],[0,6,6],[0,6,6], [6,0,0], [0,6,0], [0,0,6]]
        >>> const_votes2 = [2,4]
        >>> total_budget2 = 30
        >>> binary_search(citizen_votes2,0,1,total_budget2,0)
        [0.06666666667, [1.9999999999998863, 3.9999999999997726], [3.9999999999997726, 3.9999999999997726, 3.9999999999997726, 3.9999999999997726, 3.9999999999997726, 3.9999999999997726, 1.9999999999998863, 1.9999999999998863, 1.9999999999998863], 30.0]

        :param citizen_votes:
        :param low:
        :param high:
        :param total_budget:
        :param i: iterations
        :return:
        """
    if high >= low:

        mid = (high + low) / 2
        const_votes = c_votes(len(citizen_votes[0]), mid, total_budget)
        all_medians = find_medians(citizen_votes, const_votes)
        c = sum_medians(all_medians)

        # if i == 0:
        #     return

        if mid == 0 or mid == 1:
            return [round(mid, 11), const_votes, all_medians, round(c, 11)]

        if round(c, 11) == total_budget:
            return [round(mid, 11), const_votes, all_medians, round(c, 11)]

        elif c > total_budget:
            return binary_search(citizen_votes, low, mid, total_budget, i-1)

        else:
            return binary_search(citizen_votes, mid, high, total_budget, i-1)

    else:
        return -1


def check_fairness_group(total_budget: float, citizen_votes: List[List]) -> bool:
    """
        >>> citizen_votes1 = [[0, 0, 0,0,0,0,0,0,0,0], [0, 0, 0,0,0,0,0,0,0,0], [0, 0, 0,0,0,0,0,0,0,0]]
        >>> total_budget1 = 30
        >>> check_fairness_group(total_budget1,citizen_votes1)
        True


        :param total_budget:
        :param citizen_votes:
        :return:
        """

    num_subjects = len(citizen_votes)
    d = []
    w = 377
    for i in citizen_votes:
        d.append(i.copy())
    for i1 in range(num_subjects):
        d[i1][0] = total_budget

        for i2 in range(num_subjects):
            d[i2][1] = total_budget

            for i3 in range(num_subjects):
                d[i3][2] = total_budget

                for i4 in range(num_subjects):
                    d[i4][3] = total_budget

                    for i5 in range(num_subjects):
                        d[i5][4] = total_budget

                        for i6 in range(num_subjects):
                            d[i6][5] = total_budget

                            for i7 in range(num_subjects):
                                d[i7][6] = total_budget

                                for i8 in range(num_subjects):
                                    d[i8][7] = total_budget

                                    for i9 in range(num_subjects):
                                        d[i9][8] = total_budget

                                        for i10 in range(num_subjects):
                                            d[i10][9] = total_budget
                                            result = compute_budget(total_budget, d)
                                            if result[3] != total_budget:
                                                return False

                                            d[i10][9] = 0
                                        d[i9][8] = 0
                                    d[i8][7] = 0
                                d[i7][6] = 0
                            d[i6][5] = 0
                        d[i5][4] = 0
                    d[i4][3] = 0
                d[i3][2] = 0
                # print("in z = ", d)
            d[i2][1] = 0
        d[i1][0] = 0

    return True





if __name__ == '__main__':
    doctest.testmod()
