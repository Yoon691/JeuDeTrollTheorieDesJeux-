import random
import pulp
#pulp.solve(PULP_CBC_CMD(msg=False))
#simplex.solve(solver=PULP_CBC_CMD(msg=False))
from Helpers import Helpers

class Strategy:
    @staticmethod
    def play(self, remaining_stones,remaining_stones_player2, troll_position, player_position):
        pass


class PrudentStartegy(Strategy):
    def __init__(self):
        self.name = "Prudent Strategy"
        self.cache = {}
        
    @staticmethod
    def play(self, remaining_stones_player1, remaining_stones_player2, troll_position, player_position):
        # print('Play PrudentStartegy')
        help = Helpers(remaining_stones_player1, remaining_stones_player2, troll_position)
        # print('Play PrudentStartegy help')
        help.fill_table(self.cache)
        # print('Play PrudentStartegy help.fill_table')
        probas, strat = help.PL_final(remaining_stones_player1, remaining_stones_player2,help.table)
        # print('Play PrudentStartegy proba, strat')
        # proba = random.uniform(0, 1)
        # print('Play PrudentStartegy proba')
        print('probas : ', probas, 'strat : ', strat)
        # sum = 0
        # for i in range(len(probas)):
        #     sum += probas[i]
        #     print('sum', sum)
        #     if sum >= proba:
        #         print('strat[i]', i, ':', strat[i])
        #         return strat[i]
        return 1


class RandomStartegy(Strategy):
    def __init__(self):
        self.name = "Random Strategy"
        self.cache = {}
    @staticmethod
    def play(self, remaining_stones,remaining_stones_player2, troll_position, player_position):
        value = random.randrange(1, remaining_stones + 1)
        return value

class HumanStartegy(Strategy):
    def __init__(self):
        self.name = "Human Strategy"
        self.cache = {}
    @staticmethod
    def play(self, remaining_stones,remaining_stones_player2, troll_position, player_position):
        print("pierres restantes : ", remaining_stones)
        value = int(input())
        return value


class Random2Startegy(Strategy):
    def __init__(self):
        self.name = "Random div 2 Strategy"
        self.cache = {}
    @staticmethod
    def play(self, remaining_stones,remaining_stones_player2, troll_position, player_position):
        if remaining_stones % 2 == 0:
            value = random.randrange(1, int((remaining_stones / 2) + 1))
        else:
            value = random.randrange(1, int((remaining_stones + 1) / 2 + 1))
        return value

