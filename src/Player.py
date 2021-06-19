from Strategy import Strategy
class Player:
    def __init__(self, position, stones, strategy):
        self.position = position
        self.stones = stones
        self.strategy = strategy

    def update_stones(self, throw_stones):
        self.stones -= throw_stones 
        if self.stones <= 0:
            return True
        else:
            return False

    def get_stones(self): 
        return self.stones
    
    def setStrategy(self, strategy):
        self.strategy = strategy

    def getStrategy(self):
        return self.strategy

    def executeStrategy(self, postroll, stones_p2):
        # print('executeStrategy')
        value = self.strategy.play(self.strategy, self.stones, stones_p2, postroll, self.position)
        # print('value executeStrategy : ', value)
        return value


    