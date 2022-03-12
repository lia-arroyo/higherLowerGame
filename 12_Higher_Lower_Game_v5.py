# Higher Lower Game - Fully Working Program Version 5
# Post Usability Testing
# Created: 14/08/18

''' Changes after usability testing

- include a basic introduction / instructions
- make calculated maximum guesses more visible
        - add hl_statement function

v3:
- state the low and high number after each round

v4:
- add a penalty for not guessing the secret number (for stats)
- if user puts gets it in 1 guess, stats should say guess not guesses

v5:
- for stats, add a "DIDNT GUESS" if user didn't guess correctly

'''

'''  import modules '''
import random
import math

''' functions '''

# integer checking function
def intcheck(question, low = None, high = None):

    # set up error messages
        if low is not None and high is not None: # input must be between high and low number
            error = "Please enter an integer between {} and {}" \
                    " (inclusive)".format(low,high)
            
        elif low is not None and high is None: # input must be higher than the low number
            error = "Please enter an integer that is more than or" \
                    " equal to {}".format(low)

        elif low is None and high is not None: # input must be lower than high number, high bound only
            error = " Please enter an integer that is less than or" \
                    " equal to {}".format(high)

        else: # no upper/lower bound
            error = "Please enter an integer."


        while True:
        
            try:
                response = int(input(question))

                # checks response is not too low
                if low is not None and response < low:
                    print(error)
                    continue

                # checks response is not too high
                if high is not None and response > high:
                    print(error)
                    continue

                return response

            except ValueError:
                print(error)
                continue

# feedback statements function
def hl_statement(statement,char):
    print()
    print(char*len(statement))
    print()
    print(statement)
    print()
    print(char*len(statement))
    print

''' main routine '''
#loop entire game
keep_going = ""
while keep_going == "":

    # introduction
    title = hl_statement("*** HIGHER LOWER GAME ***","*")
    print()
    print("How to play:")
    print()
    print("- Enter a low and a high number.")
    print("- The game will randomly generate a secret number.")
    print("- Your aim is to guess the secret number correctly in the least amount of guesses as possible")
    print()
    print("The game will automatically calculate a maximum number of guesses based on the low/high you entered.")
    print("Choose your preferred number of guesses based on the calculated maximum.")
    print("Maximum number of rounds is 5.")
    print()
    print("Good luck!")
    print()

    
    # integer checking - start up of game
    rounds = intcheck("How many rounds? ", 1, 5)
    lowest = intcheck("Enter a Low number: ")
    highest = intcheck("Enter a High number: ", lowest + 1)
    
    # maximum guess calculator 
    range = highest - lowest + 1
    max_raw = math.log2(range) # finds the max guesses using log
    max_upped = math.ceil(max_raw) # rounds up max_raw using ceil (ceil aka ceiling)
    max_guesses = max_upped + 1
    print()
    maximum = hl_statement("=== The maximum number of guesses allowed for that range of numbers is {} ===".format(max_guesses),"=")

    print()
    guesses = intcheck("How many guesses do you want? ", 1, max_guesses)

    # variables
    num_won = 0
    game_stats = []
    rounds_played = 0

    while rounds_played < rounds:
        guess = ""
        guesses_left = guesses
        num_guesses = 0
        duplicates = [] 

        # generate secret number
        secret = random.randint(lowest, highest)

        # round counter
        start_round = hl_statement("### Round {} of {} ###".format(rounds_played + 1, rounds), "#")
        print("Low: {} | High: {}".format(lowest, highest))
        print()
        print("Guess the secret number. It is an integer between {} and {}.".format(lowest, highest))
        print()

        
        # if guess is incorrect and user still has guesses left
        while guess != secret and guesses_left >= 1:
            
            guess = intcheck("Guess: ", lowest, highest)

            # if user has guessed the same number
            if guess in duplicates:
                duplicate = hl_statement("!! YOU ALREADY GUESSED THAT, try again. | Guesses Left: {} !!".format(guesses_left),"!")
                continue
            
            guesses_left -= 1
            num_guesses += 1
            
            duplicates.append(guess) # adds guess to duplicates list


            # if users has guesses left
            if guesses_left >= 1:
                if guess < secret:
                    too_low = hl_statement("^^ TOO LOW. Try a higher number. | Guesses left: {} ^^".format(guesses_left),"^")
                
                elif guess > secret:
                    too_high = hl_statement("vv TOO HIGH. Try a lower number. | Guesses Left: {} vv".format(guesses_left),"v")

                else:
                    if guess < secret:
                            print("Too low!")
                    elif guess > secret:
                            print("Too high!")

            #if user guessed correctly
            if guess == secret:
                num_won += 1
                    
                if guesses_left == guesses - 1:
                    one_guess = hl_statement("== Wow! Congrats, you got it in *ONE* guess! ==","=")
                else:
                    well_done = hl_statement("~~ Congrats! You guessed the secret number in {} guesses. ~~".format(num_guesses),"~")
             

            # if user ran out of guesses
            if guess != secret and guesses_left == 0:
                print("Sorry. You don't have any guesses left. You lose.")
                print("The secret number was {}".format(secret))
                num_guesses += 1 # adds a penalty guess

        game_stats.append(num_guesses) # adds number of guesses to stats list
        print("Rounds won: {} | Rounds Lost: {}".format(num_won, rounds_played - num_won + 1))
        rounds_played += 1
                

    #!!!! END GAME MECHANICS !!!!

    # print game outcome
    print()
    print("*** Scores per Round ***")
    list_count = 1
    for item in game_stats:
        if item == 1: # if they guessed in 1 try
                print("Round {}: {} guess".format(list_count, item))
                list_count += 1

        elif item == guesses + 1: # if user didn't guess correctly
                print("Round {}: DID NOT GUESS CORRECTLY".format(list_count))
                list_count += 1
        
        else: 
                print("Round {}: {} guesses".format(list_count, item))
                list_count += 1

    # calculating stats

    game_stats.sort()
    best = game_stats[0]
    worst = game_stats[-1]
    average = sum(game_stats)/len(game_stats)

    print()
    print("*** Stats ***")
    # best score
    if best == 1: # if guess is 1
            print("Best: {} guess".format(best))

    elif best == guesses + 1: # if best score is user did not guess correctly
            print("Best: {} guessses - DID NOT GUESS CORRECTLY".format(best))

    else:
            print("Best: {} guesses".format(best))
            
    # worst score
    if worst == 1: # if guess is 1
            print("Worst: {} guess".format(worst))
            
    elif worst == guesses + 1: # if worst is user did not guess correctly
            print("Worst: {} guessses - DID NOT GUESS CORRECTLY".format(worst))
    else:
            print("Worst: {} guesses".format(worst))

    # average score
    if average == 1:
            print("Average: {:.2f} guess".format(average))
    else:
            print("Average: {:.2f} guesses".format(average))

    print()
    print("Game over!")
    keep_going = input("Press <enter> to play again or any key to quit. ")
    print()

