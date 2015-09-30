#http://www.codeskulptor.org/#user40_8ou8cZTONN_53.py
import simplegui
import math
import random

this_guess = 0
remaining_guesses = 0
this_answer = 0
game_range = 100
won = False

# helper function to start and restart the game
def new_game():
    # initialize global variables
    global this_guess
    global remaining_guesses
    global this_answer
    global game_range
    if game_range == 100:
        remaining_guesses = 7
    elif game_range == 1000:
        remaining_guesses = 10
    this_answer = random.randrange(0, game_range)
    print "Guess the number from 0 to %s, you have %s guesses" % (game_range, remaining_guesses)
    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global game_range
    game_range = 100
    new_game()
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global game_range
    game_range = 1000
    new_game()
    pass
    
def input_guess(guess):
    global this_guess
    global remaining_guesses
    global this_answer
    global won
    if remaining_guesses > 0:
        this_guess = int(guess)
        if this_answer > this_guess:
            print "Guess was %s, answer is Higher. %s guesses remaining" % (this_guess, (remaining_guesses - 1))
        elif this_answer < this_guess:
            print "Guess was %s, answer is Lower. %s guesses remaining" % (this_guess, (remaining_guesses - 1))
        elif this_answer == this_guess:
            print "Guess is %s, that is Correct!\n" % this_guess
            new_game()
        else:
            print "Error"
        remaining_guesses -=1
    if remaining_guesses == 0:
        if won:
            #this code will never be executed even if the above check for correctness didn't initialize a new game, I'm not sure why
            print "You win!"
            new_game()
        else:
            print "You lose, the answer was %s\n" % this_answer
            new_game()
    pass

    
# create frame
def draw_frame():
    global frame
    frame = simplegui.create_frame("Pick A Number", 200, 200)
    frame.add_button("[0, 100]", range100, 100)
    frame.add_button("[0, 1000]", range1000, 100)
    frame.add_input("Guess", input_guess, 100)

# call new_game 
new_game()

draw_frame()