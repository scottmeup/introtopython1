#http://www.codeskulptor.org/#user40_93Y6mtR89k7cYFb.py


import random

def rpsls(name):
    #Take the player choice and convert it to an integer, generate a random int for the
    #computer. Assign a string that represents computers choice
    playerChoiceInt = name_to_number(name)
    computerChoiceInt = random.randint(0, 4)
    player_choice = name
    computer_choice = number_to_name(computerChoiceInt)
    
    #Distill the result to a number between 0-4
    result = (playerChoiceInt - computerChoiceInt) % 5
    
    #Log the choices in words to console
    print ("Player chooses %s") % player_choice
    print ("Computer chooses %s") % computer_choice
    
    #
    if playerChoiceInt == computerChoiceInt:
        print("Player and computer tie!\n")
    elif ((result>0) and (result<3)):
        print("Player Wins!\n")
    elif ((result>2) and (result<5)):
        print("Computer Wins!\n")
    else:
        print("I was hoping this block would never be reached!\n")
        
    
    print "Player: %s, Computer: %s, Result: %s %s" % (playerChoiceInt, computerChoiceInt, result, "\n")
    #0 = Draw
    #1 = Player Wins
    #2 = Player Wins
    #3 = Player Looses
    #4 = Player Looses
        


    
def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return None


        
def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'Spock'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return None

#Run the test as many times as the argument 'runs'
def test_rpls(runs):
	print "#################"
	for x in xrange(0, runs):
		print "*** Test %s of %s ***" % (x+1, runs)
		rpsls('rock')
		rpsls('Spock')
		rpsls('paper')
		rpsls('lizard')
		rpsls('scissors')
    
#run the test x amount of times
test_rpls(10)