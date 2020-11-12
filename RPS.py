# The example function below keeps track of the opponent's history and plays
 # whatever the opponent played two plays ago. It is not a very good player
 # so you will need to change the code to pass the challenge.
import random
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    # if len(opponent_history) == 2:
    #     guess= 'P'

    if len(opponent_history) > 2:
        if opponent_history[-1] == opponent_history[-2] == ('S' or 'P'):
            guess = "R"
            return guess
        if opponent_history[-1] == opponent_history[-2] == ('R'):
            guess = random.choice(["R", "S"])
            return guess
        guess =opponent_history[-(random.randint(1, len(opponent_history)))]
        if
        return guess
    return guess
