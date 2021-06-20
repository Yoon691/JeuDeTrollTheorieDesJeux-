from Player import Player
from Troll import Troll
from Strategy import Strategy,PrudentStartegy, RandomStartegy,PlusDivStartegy, Random2Startegy, HumanStartegy, DivStartegy


class Game:
    def __init__(self, grid_size, init_stones):
        self.winner = None
        self.grid_size = grid_size
        self.init_stones = init_stones
        self.player_1 = Player(-(self.grid_size - 1) / 2, init_stones,
                               PrudentStartegy())
        self.player_2 = Player((self.grid_size - 1) / 2, init_stones,
                               PrudentStartegy())
        print('Strategic player 1 :', self.player_1.strategy.name, 'VS', 'Strategic player 2 : ', self.player_2.strategy.name)
        self.troll = Troll(0)

    def start_game(self):
        round = False
        nb_round = 1
        while (not round):
            print('\nRound ', nb_round)
            round = self.game_round()
            nb_round += 1
        if self.winner == None:
            print("Match nul")
            return 0
        else:
            print("Player", self.winner, " gagne !")
            return self.winner

    def set_winner(self):
        num = None
        if self.troll.getPostion() ==  (self.grid_size - 1) / 2:
            num = 1
        elif self.troll.getPostion() ==  -(self.grid_size - 1) / 2:
            num = 2
        elif self.player_1.get_stones() == self.player_2.get_stones():
            num = None
        elif self.player_1.get_stones() == 0:
            if self.player_2.get_stones() == self.troll.getPostion():
                num = None
            elif self.player_2.get_stones() < self.troll.getPostion():
                num = 1
            else:
                num = 2
        elif self.player_2.get_stones() == 0:
            if self.player_1.get_stones() + self.troll.getPostion() < 0:
                num = 2
            elif self.player_1.get_stones() + self.troll.getPostion() == 0:
                num = None
            else:
                num = 1
        self.winner = num

    def get_winner(self):
        return self.winner

    def game_round(self):
        print("Troll position avant: ", self.troll.getPostion())
        print('picked_stones_player_1')
        picked_stones_player_1 = self.player_1.executeStrategy(
            int(self.troll.getPostion()), self.player_2.get_stones())
        print('picked_stones_player_2')
        picked_stones_player_2 = self.player_2.executeStrategy(
            int(self.troll.getPostion()), self.player_1.get_stones())
        print("Player 1: ", picked_stones_player_1, " - Player 2: ",
              picked_stones_player_2)
        loose_player1 = self.player_1.update_stones(picked_stones_player_1)
        loose_player2 = self.player_2.update_stones(picked_stones_player_2)

        self.troll.move(picked_stones_player_1, picked_stones_player_2)
        print("Troll position : ", self.troll.getPostion())

        if loose_player1 or loose_player2:
            self.set_winner()
            return True
        elif abs(self.troll.getPostion()) == (self.grid_size - 1) / 2:
            self.set_winner()
            return True
        return False
