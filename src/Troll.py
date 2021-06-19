class Troll:
    def __init__(self, position):
        self.position = position

    def move(self, stones_player1, stones_player2):
        if stones_player1 > stones_player2 : 
            self.position += 1
        elif stones_player1 < stones_player2:
            self.position -= 1 
        return self.position
    
    def getPostion(self):
        return self.position