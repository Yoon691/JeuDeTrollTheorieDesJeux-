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
        proba = random.uniform(0, 1)
        # print('Play PrudentStartegy proba')
        print('proba : ', proba, 'probas : ', probas, 'strat : ', strat)
        sum = 0
        for i in range(len(probas)):
            sum += probas[i]
            if sum >= proba:
                return strat[i]
        return 1

class DivStartegy(Strategy):
    def __init__(self):
        self.name = "Division Strategy"
    @staticmethod
    def play(self, remaining_stones,remaining_stones_player2, troll_position, player_position):
        if remaining_stones == 1:
            return 1
        if remaining_stones % 2 == 0:
            value = int(remaining_stones / 2)
        else:
            value = int((remaining_stones - 1) / 2)
        return value


class RandomStartegy(Strategy):
    def __init__(self):
        self.name = "Random Strategy"
    @staticmethod
    def play(self, remaining_stones,remaining_stones_player2, troll_position, player_position):
        value = random.randrange(1, remaining_stones + 1)
        return value

class HumanStartegy(Strategy):
    def __init__(self):
        self.name = "Human Strategy"
    @staticmethod
    def play(self, remaining_stones,remaining_stones_player2, troll_position, player_position):
        print("pierres restantes : ", remaining_stones)
        value = int(input())
        return value


class Random2Startegy(Strategy):
    def __init__(self):
        self.name = "Random div 2 Strategy"
    @staticmethod
    def play(self, remaining_stones,remaining_stones_player2, troll_position, player_position):
        if remaining_stones % 2 == 0:
            value = random.randrange(1, int((remaining_stones / 2) + 1))
        else:
            value = random.randrange(1, int((remaining_stones + 1) / 2 + 1))
        return value


class PlusDivStartegy(Strategy):
    def __init__(self):
        self.first = True
        self.name = "Plus Division Strategy"
    @staticmethod
    def play(self, remaining_stones,remaining_stones_player2, troll_position, player_position):
        if self.first:
            self.first = False
            self.prev_position = troll_position
            if remaining_stones % 2 == 0:
                self.value = random.randrange(1,
                                              int((remaining_stones / 2) + 1))
            else:
                self.value = random.randrange(
                    1, int((remaining_stones + 1) / 2 + 1))
        else:
            prev_dist = abs(self.prev_position - player_position)
            new_dist = abs(troll_position - player_position)
            if prev_dist <= new_dist:
                if self.value % 2 == 0:
                    self.value = int(self.value / 2)
                else:
                    self.value = int((self.value + 1) / 2)
            else:
                if self.value + 1 >= remaining_stones:
                    if self.value % 2 == 0:
                        self.value = int(self.value / 2)
                    else:
                        self.value = int((self.value + 1) / 2)
                else:
                    self.value += 1

        return self.value
