
import math
import random
import numpy as np


def orderly_division(player_a, player_b, division_player_a, division_player_b):


    minimum_object_A_index, maximum_object_B_index = search_minimumA_maximumB_objects(player_a, player_b,
                                                                                      division_player_a,
                                                                                      division_player_b)
    minimumA = player_a[minimum_object_A_index] / player_b[minimum_object_A_index]
    maximumB = player_a[maximum_object_B_index] / player_b[maximum_object_B_index]
    if minimumA < maximumB:
        return share_minimal(player_a, player_b, division_player_a, division_player_b, minimum_object_A_index,
                             maximum_object_B_index)

    return True


def search_minimumA_maximumB_objects(player_a, player_b, division_player_a, division_player_b):
    maximum = 0
    minimum = math.inf
    index_object1 = 0
    index_object2 = 0
    for i in range(len(player_a)):
        if minimum > (player_a[i] / player_b[i]) and division_player_a[i] > 0:
            minimum = (player_a[i] / player_b[i])
            index_object1 = i
        if maximum < (player_a[i] / player_b[i]) and division_player_b[i] > 0:
            maximum = player_a[i] / player_b[i]
            index_object2 = i

    return index_object1, index_object2


def share_minimal(player_a, player_b, division_player_a, division_player_b, minimum_object_A_index,
                  maximum_object_B_index):
    va1 = player_a[minimum_object_A_index]
    va2 = player_a[maximum_object_B_index]
    vb1 = player_b[minimum_object_A_index]
    vb2 = player_b[maximum_object_B_index]

    while True:
        z = 0.1
        y = 0.9
        z_floor = math.floor(z * 10) / 10
        y_floor = math.floor(y * 10) / 10
        if y_floor > 0 and z_floor > 0 and (va1 / va2) < z_floor / y_floor < (vb1 / vb2):
            if y_floor <= division_player_a[minimum_object_A_index] and z_floor <= division_player_b[
                maximum_object_B_index]:
                break

    new_division_player_a = division_player_a.copy()
    new_division_player_b = division_player_b.copy()
    new_division_player_a[minimum_object_A_index] -= y_floor
    new_division_player_b[minimum_object_A_index] += y_floor
    new_division_player_a[maximum_object_B_index] += z_floor
    new_division_player_b[maximum_object_B_index] -= z_floor

    txt = "Pareto improvement: Player A transfers {} of object {} to player B, and player B transfers {} of object {} to player A"
    print(txt.format(y_floor, minimum_object_A_index, z_floor, maximum_object_B_index))
    txt = "The improvement after the division: player A - {} , player B - {}"
    print(txt.format(new_division_player_a, new_division_player_b))
    check_pareto_improvement(player_a, player_b, division_player_a, division_player_b, new_division_player_a,
                             new_division_player_b)
    return new_division_player_a, new_division_player_b


def check_pareto_improvement(player_a, player_b, division_player_a, division_player_b, new_division_player_a,
                             new_division_player_b):
    new_sum_a = 0
    new_sum_b = 0
    old_sum_a = 0
    old_sum_b = 0
    for i in range(len(player_a)):
        old_sum_a += player_a[i] * division_player_a[i]
        old_sum_b += player_b[i] * division_player_b[i]
        new_sum_a += player_a[i] * new_division_player_a[i]
        new_sum_b += player_b[i] * new_division_player_b[i]

    if (new_sum_a > old_sum_a and new_sum_b >= old_sum_b) or (new_sum_b > old_sum_b and new_sum_a >= old_sum_a):
        txt = "old sum A = {} , new sum A = {} , old sum B = {} , new sum B {}"
        return print(txt.format(old_sum_a, new_sum_a, old_sum_b, new_sum_b))

    else:
        print("Not a Pareto improvement")
        txt = "old sum A = {} , new sum A = {} , old sum B = {} , new sum B {}"
        return print(txt.format(old_sum_a, new_sum_a, old_sum_b, new_sum_b))


def find_z_find_y(min,max):
    z = 0.1
    y = 0.9
    if()

if __name__ == '__main__':
    import doctest

    doctest.testmod()