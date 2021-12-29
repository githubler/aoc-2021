#day 21

from functools import lru_cache


class Dice():

    def __init__(self):
        self.num_rolled = 0
        self.last_rolled = 0

    def roll(self):
        result = 0
        for i in range(3):
            rolled = (self.last_rolled+1)%100
            if rolled == 0:
                rolled = 100
            self.last_rolled = rolled
            self.num_rolled += 1
            result += self.last_rolled

        return result, self.num_rolled


class Player():

    def __init__(self, start):
        self.score = 0
        self.space = start

    def get_score(self):
        return self.score

    def move(self, steps):
        new_space = (self.space + steps)%10
        if new_space == 0:
            new_space = 10
        self.space = new_space
        self.score += self.space


#
# part 1
#
dice = Dice()
player1 = Player(10)
player2 = Player(2)

for i in range(10000):
    result, num_rolled = dice.roll()
    player1.move(result)
    if player1.get_score() >= 1000:
        score = player2.get_score()
        submit = num_rolled * score
        print("Submit: ", submit)
        break

    result, num_rolled = dice.roll()
    player2.move(result)
    if player2.get_score() >= 1000:
        score = player1.get_score()
        submit = num_rolled * score
        print("Submit: ", submit)
        break


#
# part 2
#
@lru_cache(maxsize=None)
def play_quantum_game(pos1, pos2, score1, score2):
    if score1 >= 21:
        return (1,0)
    elif score2 >= 21:
        return (0,1)
    else:
        wins = (0,0)
        for dice1 in range(1,4):
            for dice2 in range(1,4):
                for dice3 in range(1,4):
                    dice_sum = dice1+dice2+dice3
                    new_pos = (pos1 + dice_sum)%10
                    if new_pos == 0:
                        new_pos = 10
                    num_world_1, num_world_2 = play_quantum_game(pos2, new_pos, score2, score1+new_pos)
                    wins = (wins[0]+num_world_2, wins[1]+num_world_1)
    return wins
    

player1 = Player(10)
player2 = Player(2)    
wins = play_quantum_game(10, 2, 0, 0)
print("Submit: ", max(wins[0], wins[1]))

