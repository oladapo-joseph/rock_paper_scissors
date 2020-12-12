# The example function below keeps track of the opponent's history and plays
 # whatever the opponent played two plays ago. It is not a very good player
 # so you will need to change the code to pass the challenge.
import random
play = []
ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    if len(opponent_history) > 2:
        if opponent_history[-1] == opponent_history[-2] =='S':
            # guess = random.choice(["R", opponent_history[-3]])
            guess = 'R'
            # return guess
        elif opponent_history[-1] == opponent_history[-2] == 'R':
            # guess = random.choice(["P",opponent_history[-3]])
            guess = 'P'
            # return guess
        elif opponent_history[-1] == opponent_history[-2] == 'P':
            # guess = random.choice(["S", opponent_history[-3]])
            guess = 'S'
            # return guess
        else:
            # guess = random.choice(['R','P', 'R','S', 'R', 'P','R','P'])
            # ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

            if (prev_play =='') or (opponent_history[-2] == ''):
                guess = ideal_response[opponent_history[-3]] #2/3
                # return guess
            else:
                if   opponent_history[-3] == '':
                    guess = ideal_response[opponent_history[-2]]
                else:
                    guess = ideal_response[prev_play]
                    # guess = prev_play
                    # guess = random.choice([ideal_response[opponent_history[-3]],ideal_response[opponent_history[-2]]])
                # return guess
    else:
        guess = 'P'

    play.append(guess)
        # if play.count(guess)> (len(play)/3):
        #     guess = ideal_response[guess]
    return guess
