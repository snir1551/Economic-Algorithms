from typing import Dict


class Player:
    def __init__(self, number_id, money):
        self.number_id = number_id
        self.money = money

    def try_buy_item(self, money):
        self.money -= money

    def get_back_money(self, money):
        self.money += money

    def __str__(self):
        print(self.number_id)


class Players:

    def __init__(self):
        self.players: list[Player] = list()
        self.max1 = 0
        self.player_max1 = 0
        self.max2 = 0

    def add_player(self, player: Player):  # add option
        self.players.append(player)
        if self.max1 < player.money:
            self.max2 = self.max1
            self.max1 = player.money
            self.player_max1 = player.number_id
        elif player.money > self.max2:
            self.max2 = player.money

    def value(self, player_number: int) -> float:  # return value of option
        if self.players[player_number] is None:  # option doesn't exist
            return -1
        return self.players[player_number].money

    def __str__(self):
        s = ""
        for i in self.players:
            s += str(i.money)
            s += str(" ")
        return s


def strategy_tender_algorithm(players: Players, player1: int) -> list:
    """
    >>> player_1 = Player(0,10)
    >>> player_2 = Player(1,20)
    >>> players_1 = Players()
    >>> players_1.add_player(player_1)
    >>> players_1.add_player(player_2)
    >>> strategy_tender_algorithm(players_1,0)
    [20.0, 10.0]

    >>> player_1 = Player(0,20)
    >>> player_2 = Player(1,10)
    >>> players_1 = Players()
    >>> players_1.add_player(player_1)
    >>> players_1.add_player(player_2)
    >>> strategy_tender_algorithm(players_1,0)
    [14.5, 15.5]

    >>> player_1 = Player(0,20)
    >>> player_2 = Player(1,10)
    >>> player_3 = Player(2,15)
    >>> players_1 = Players()
    >>> players_1.add_player(player_1)
    >>> players_1.add_player(player_2)
    >>> players_1.add_player(player_3)
    >>> strategy_tender_algorithm(players_1,0)
    [9.333333333333332, 15.333333333333332, 20.333333333333332]

    >>> player_1 = Player(0,20)
    >>> player_2 = Player(1,20)
    >>> player_3 = Player(2,15)
    >>> players_1 = Players()
    >>> players_1.add_player(player_1)
    >>> players_1.add_player(player_2)
    >>> players_1.add_player(player_3)
    >>> strategy_tender_algorithm(players_1,0)
    [6.666666666666667, 26.666666666666668, 21.666666666666668]

    :param players:
    :param player1:
    :return:
    """
    devide_money = 0
    if players.players[player1].money == players.max1 and players.max1 != players.max2:
        for p in players.players:
            if p.number_id == player1:
                devide_money += players.max2 + 1
                p.try_buy_item(players.max2 + 1)

        devide_money = devide_money / len(players.players)
        for p in players.players:
            p.get_back_money(devide_money)
    else:
        players.players[players.player_max1].try_buy_item(players.max1)
        devide_money = players.max1 / len(players.players)
        for p in players.players:
            p.get_back_money(devide_money)

    result = []
    for i in players.players:
        result.append(i.money)

    return result


if __name__ == '__main__':
    import doctest

    doctest.testmod()
