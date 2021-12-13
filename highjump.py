print("")
print("  High Jump") 
print("") 
height = 10 
jump_failed = False 
win_cond = False 
possible_skips = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30] 
tries = 0 
height_bool = False
attempt_fail = False
height_test = 10
print("Initial height is 10, after this turn you may skip.") 
print("Input 'roll' to roll your dice.") 
print("")
print("Input 'help' to view various game functions.") 
while win_cond == False:
    import random 
    d1 = random.randint(1,6) # random module 
    d2 = random.randint(1,6) 
    d3 = random.randint(1,6)
    d4 = random.randint(1,6)
    d5 = random.randint(1,6)
    L = [d1, d2, d3, d4, d5]  
    total = d1 + d2 + d3 + d4 + d5   # adds dice
    print("")
    move = str(input("Move: "))
    move = move.upper()
    print("") 
    if move == "ROLL":
        print("Current Height: " + str(height))
    while move =="ROLL" and tries <= 3:
        print("You rolled: " + str(L)) 
        print("You scored a " + str(total))
        if total >= height:
            print("You cleared " + str(height) + " feet.") 
            attempt_fail = False
            tries = 0
            break
        elif total < height:
            print("You failed to clear " + str(height) + " feet.") 
            tries = tries + 1 
            if tries < 3:
                print("Next Try") 
            attempt_fail = True
            break 
        if tries == 3:
            break
    if tries == 3:
        print("")
        print("Your 3 attempts are up.")
        print("You maxed out at " + str(height_test) + " feet.") 
        print(str(height_test) + " is your final score.")
        break
    if move == "ROLL" and attempt_fail == False:
        height_test = height                        # Keeps track of the user's current H.S
        height = height + 2   
        tries = 0
        print("")        
        skip = str(input("The height has increased by 2, would you like to skip to a greater value? "))
        skip = skip.upper()
        if skip == "YES":
            print("Possible Skips: " + str(possible_skips))
            while height_bool == False:                             # This while loop uses a boolean value
                height = int(input("Skip to: "))                    # to make sure any skip input is valid
                if height <= height_test:
                    print("Invalid Input, you cannot skip to less or equal to your current best.") 
                    height_bool = False
                elif height > 30:
                    print("Invalid Input, you cannot go past 30 feet.") 
                    height_bool = False 
                    print("")
                elif height % 2 == 1:
                    print("Invalid Input, you can only skip to even numbers.") 
                    height_bool = False
                    print("")
                else:
                    print("Height skipped to " + str(height)) 
                    height_bool = True
            height_bool = False
        elif skip == "EXIT":
            print("Game Exited")
            exit()
        else:
            print("No skip, height is up 2 feet.") 
    if move != "ROLL" and move != "EXIT" and move != "HELP" and move != "HIGHSCORE":
        print("Incorrect Input") 
    if move == "EXIT":
        print("") 
        print("Game Exited")
        break 
    if move == "HELP":              # Help function
        print("| HELP |") 
        print("")  
        print("FUNCTION - INPUT")
        print("")
        print("Roll Dice - roll")
        print("Help - help")
        print("Settings - settings") 
        print("Close Game - exit")
        print("Current Highscore - highscore")
   
    if move == "SETTINGS":
        print("| SETTINGS |") 
        print("")
        print("1. ")
    if move == "HIGHSCORE":
        print("Current Highscore: " + str(height_test))
