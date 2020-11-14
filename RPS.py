# The example function below keeps track of the opponent's history and plays
 # whatever the opponent played two plays ago. It is not a very good player
 # so you will need to change the code to pass the challenge.
import random
play = []
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)


    if len(opponent_history) > 2:
        if opponent_history[-1] == opponent_history[-2] =='S':
            guess = random.choice(["R", opponent_history[-3]])
            # guess = 'R'
            return guess
        elif opponent_history[-1] == opponent_history[-2] == 'R':
            guess = random.choice(["P",opponent_history[-3]])
            # guess = 'P'
            return guess
        elif opponent_history[-1] == opponent_history[-2] == 'P':
            guess = random.choice(["S", opponent_history[-3]])
            # guess = 'S'
            return guess
        else:
            # guess = opponent_history[-(random.randint(1,4))]
            # guess = random.choice(opponent_history)
            guess = random.choice(['R', 'P', 'S'])
            return guess
    else:
        guess = 'P'

    play.append(guess)
    return guess
