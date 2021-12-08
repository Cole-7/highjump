print("  High Jump") 
print("") 
height = 10 
jump_failed = False 
win_cond = False 
possible_skips = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30] 
tries = 0
print("Initial height is 10, after this turn you may skip.") 
print("Input 'roll' to roll your dice.")
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
    print("Current Height: " + str(height))
    while move =="ROLL" and tries <= 3:
        print("You rolled: " + str(L)) 
        print("You scored a " + str(total))
        if total >= height:
            print("You cleared " + str(height) + " meters.") 
        elif total < height:
            print("You failed to clear " + str(height) + " meters.") 
            tries = tries + 1 
            if tries < 3:
                print("Next Try") 
        if tries == 3:
            print("Your 3 attempts are up.")
            print("You maxed out at " + str(height) + " meters.") 
            break
    height = height + 2 
    tries = 0
    skip = str(input("The height has increased by 2, would you like to skip to a greater value? "))
    #print("Possible Skips: " + str(possible_skips))
    #height = int(input("Skip to: ")) 
