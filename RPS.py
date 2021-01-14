# The example function below keeps track of the opponent's history and plays
 # whatever the opponent played two plays ago. It is not a very good player
 # so you will need to change the code to pass the challenge.
import random
play = []
ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    if len(opponent_history) > 2:
        if opponent_history[-1] == opponent_history[-2]:
            guess = ideal_response[opponent_history[-1]]

        else:
            if (prev_play =='') or (opponent_history[-2] == ''):
                guess = ideal_response[opponent_history[-3]] #2/3

            else:
                if   opponent_history[-3] == '':
                    guess = ideal_response[opponent_history[-2]]
                else:
                    guess = random.choice([ideal_response[prev_play], prev_play])
                    # guess = ideal_response[prev_play]
                    # guess = random.choice([ideal_response[opponent_history[-3]],ideal_response[opponent_history[-2]]])
                # return guess
    else:
        guess = 'P'

    play.append(guess)

    return guess
