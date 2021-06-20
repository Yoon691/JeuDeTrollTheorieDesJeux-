from Game import Game
def main():
    p1 = 0
    p2 = 0
    nul = 0
    nb = 100
    cacheJ1 = None
    cacheJ2 = None
    for i in range(nb):
        print('nombre partie a jouer : ', nb)
        game = Game(7, 30)
        print('Start partie : ', i + 1)
        if cacheJ1 is not None : 
            game.player_1.strategy.cache = cacheJ1
            #print('cacheJ1 Debut paritie : ', cacheJ1)
        if cacheJ2 is not None : 
            game.player_2.strategy.cache = cacheJ2
            #print('cacheJ2 Debut partie : ', cacheJ2)
        val = game.start_game()
        if val == 0: 
            nul += 1
        elif val == 1:
            p1 += 1
        else:
            p2 += 1
        print('Fin partie n : ', i + 1)
        if game.player_1.strategy.cache is not None :
          cacheJ1 = game.player_1.strategy.cache
          # print('cacheJ1 Fin partie : ', cacheJ1)
        if game.player_2.strategy.cache is not None :
          cacheJ2 = game.player_1.strategy.cache
          # print('cacheJ2 Fin paritie : ', cacheJ2)
    print('resultat de councours')
    print(p1/nb," - ", nul/nb, " - ", p2/nb)

main()
