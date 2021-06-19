from test import test
import random

def play(remaining_stones):
    return random.randrange(1, remaining_stones+1)
Test = test("Ahmed", "Saadallah") 
stones = 15 
stones -= 2
print(stones)
"""while stones > 0:
    randomVal = play(stones)
    print(stones ," - " ,  randomVal)
    stones -= randomVal 
"""