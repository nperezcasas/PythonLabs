# COMS 103
# Nuria Perez Casas
# Program 1


def human_choice():
    """Asks the user for an input, gets the choice from the user, it
    has input validation and no parameters.

    It returns either 'rock', 'paper', or 'scissors'.
    """
    while True:
        # Ask the user for some input and return either rock, paper, scisors
        response = input("Enter 'rock', 'paper' or 'scissors': ")

        # We use .lower() to accept any response ROCK Rock r R
        
        if response.lower() == "rock" or response.lower() == "r":
            return 'rock'
        elif response.lower() == "paper" or response.lower() == "p":
            return 'paper'
        elif response.lower() == "scissors" or response.lower() == "s":
            return 'scissors'
        # print an error message to let the user know they messed up.
        # We use this input validation so that the program doesn't crash
        # if the response is wrong. 
        else:
            print("That is not an accepted answer. Try again.")
            
import random # We will need random so we import it. 

def computer_choice():
    """ Generates a random choice for the computer.

    It will be returned either 'rock', 'paper' or 'scissors'
    """
    options = ['rock', 'paper', 'scissors']
    choice = random.choice(options)
    return choice


def winner(human_choice, computer_choice):
    """This function determines the winner of one play of the game.
     It contains two parameters: human_choice and computer_choice.

     It returns the winner of the round 'computer', 'you'(human), or 'tie'.
     """
    # We basically use if/elif with all the possibe options and we
    # determine the outcomes and return them. 
    
    if human_choice == computer_choice:
       return "tie"
    elif human_choice == "rock" and computer_choice == "scissors":
       return "you"
    elif human_choice == "paper" and computer_choice == "scissors":
        return "computer"
    elif computer_choice == "rock" and human_choice == "paper":
        return "computer"
    elif human_choice == "scissors" and computer_choice == "paper":
        return "you"
    elif computer_choice == "paper" and human_choice == "rock":
       return "you"
    elif computer_choice == "scissors" and human_choice == "rock":
       return "computer"

def one_round():
    """This function manages one round of the game. No parameter. It calls
    the three function above and prints the choices made by computer and human,
    prints useful information and returns the result of this
    one round, either ‘computer’, ‘human’, or ‘tie’.
    """
    # We call the three previous functions. 
    choice = computer_choice()
    response = human_choice()
    win = winner(response, choice)
    # print useful information. 
    print()
    print("You chose ", response)
    print("The computer chose ", choice)
    print()
    # We use the returned information from the winner function to
    # print who won the round and to use it in the accumulator function. 
    if win == "you":
        print("Good job! You won!")
    elif win == "computer":
        print("Sorry the computer wins... Keep trying")
    elif win == "tie":
        print("It's a tie, try again!")        
        
    return win

def score_master():
    """Manages multiple rounds of the game. We call this function to start the
    game. No parameters. set up the game, welcome the user, keep track of the
    score, and ask the user if he or she wishes to play again. When the user
    doesn’t wish to play again, this function will print the final score.
    """
    
    print("Welcome to the Rock, Paper, Scissors Game!")
    print("Follow the instructions to play against the computer")
    print()
    # We use an accumulator function to keep the score of the multiple rounds.
    comp_score = 0
    human_score = 0
    tie_score = 0

    while True:
        # We create a loop that will run the program until the user says no.
        rounds = one_round()
        
        keep_playing = input("Do you want to keep playing? Enter yes or no: ")
        print()
        # We keep the score along the different rounds.
        if rounds == 'you':
            human_score += 1
        elif rounds == 'computer':
            comp_score += 1
        elif rounds == 'tie':
            tie_score += 1

        # We ask the user if they want to keep playing and if they do we
        # continue the loop and if not we break it and we print the final
        # score.
        # We also include input validation in case they mess up when we ask
        # if they want to keep playing.
        
        if keep_playing.lower() == "yes" or keep_playing.lower() == "y":
            continue
        elif keep_playing.lower() == "no" or keep_playing.lower() == "n":
            break
        else:
            print("Sorry I didn't understand you")
            
    print("The scoreboard was this: ")
    print("You won a total of ", str(human_score), "times")
    print("The computer won ", str(comp_score), "times")
    print("You had ", str(tie_score), "ties")
    print()
    print("Thank you for playing and we hope to see you again!")
    
if __name__ == "__main__":
    score_master() 
    
