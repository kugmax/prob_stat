# This starter code was written by Alex Tsun for CSE 312 Summer 2020.

# Student Name: ____
# UW Email    : ____@uw.edu

# =============================================================
# You may define helper functions, but DO NOT MODIFY
# the parameters or names of the provided functions.
# The autograder will expect that these functions exist
# and attempt to call them to grade you.

# Do NOT add any import statements.
# =============================================================

import numpy as np
import matplotlib.pyplot as plt

def part_a(n:int=21, p:float=0.3, ntrials:int=5000):
    """
    Write code to simulate a ping pong game to n points,
    where the probability of you winning a single point is p.
    You must win by 2; for example, if the score is 21 − 20, 
    the game isn’t over yet. Simulate ntrials # of games.

    :param n: The number of points to play to.
    :param p: The probability of YOU winning a single point.
    :param ntrials: The number of trials to simulate.
    :return: returns the probability YOU win the overall game.

    You can ONLY use the function np.random.rand() to generate randomness; 
    this function generates a random float from the interval [0, 1).
    """

    def sim_one_game():
        """
        This is a nested function only accessible by parent sim_prob,
        which we're in now. You may want to implement this function!
        """
        player_1_points = 0
        player_2_points = 0
        while True:
            r = np.random.rand()
            if r < p:
                player_1_points = player_1_points + 1
            else:
                player_2_points = player_2_points + 1

            if player_1_points + player_2_points >= n and np.abs(player_1_points - player_2_points) > 1:
                return 1 if player_1_points > player_2_points else 0

    won_games = 0
    for i in range(ntrials):
        won_games += sim_one_game()

    return won_games / ntrials

def part_b():
    """
    Make a single plot using matplotlib with the x-axis being p
    for different values of p in {0, 0.04, 0.08,...,0.96, 1.0} 
    and the y-axis being the probability of winning the overall game 
    (use your previous function). Plot 3 “curves” in different colors, 
    one for each n in {3,11,21}.

    You can code up your solution to part (b) here, but this
    will not be autograded. Make sure to label your axes
    and title your plot appropriately, as well as include a 
    legend! Include your resulting plot in the written submission.

    Hint(s):
    1. You'll call plt.plot(...) 3 times total, one for each
    n. Make sure your calls are of the form:
    'plt.plot(x_vals, y_vals, "-b", label="n=11")' where "-b" indicates
    blue and "n=11" is to say these set of points is for n=11. You may 
    want to use "-r", "-g", and "-b", a different color for each n.
    2. Use plt.legend(loc="upper left").
    3. Use plt.savefig(...).

    :return: Nothing. Just save the plot you made!
    """
    def generate(n, step=4):
        result = dict()
        for i in range(0, 100+step, step):
            p = i / 100
            result[p] = part_a(n=n, p=p)

        return result

    n_3_prob = generate(n=3)
    n_11_prob = generate(n=11)
    n_21_prob = generate(n=21)

    plt.plot(n_3_prob.keys(), n_3_prob.values(), "-b", label="n=3")
    plt.plot(n_11_prob.keys(), n_11_prob.values(), "--r", label="n=11")
    plt.plot(n_21_prob.keys(), n_21_prob.values(), "-.g", label="n=21")

    plt.legend(loc="upper left")
    plt.savefig('ping_pong.png')

if __name__ == '__main__':
    # You can test out things here. Feel free to write anything below.
    print(part_a())
    part_b()
