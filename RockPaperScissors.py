# This is a simple re-enactment of the classic game: Rock Paper Scissors
# Rock...Paper...Scissor...Shoot!
# Player has to enter r, s or p into the terminal upon 'Shoot' to match against the Computer
# Each win +1 to points earned
# Game over if Player loses
# Keeps track of highest score 

# Initializes highest score in score.txt
import shelve
#data = shelve.open('score.txt')
#data['highest_score'] = 0
#data.close()

# Delays 'Rock...Paper...Scissors...Shoot!' message
import time
import sys
def message(string) :

    # Printing char by char
    for i in string :
        if i != '.' :
            print(i, end="")
        else :
            time.sleep(0.2)
            print(i,end="")
            sys.stdout.flush()

# Main loop
winning = True
score = 0
print("Game starting")
while winning :

    # Display game prompt
    message("Rock...Paper...Scissors...Shoot!")

    # Randomly select Computer choice
    import random
    choice_list = ["Rock", "Paper", "Scissors"]
    computer = random.sample(choice_list, k=1)[0]
    print("")

    # Get Player choice
    player = input("")

    # Computer vs Player
    if player != "" :

        # Player wins
        if (player == "r" and computer == "Scissors") or (player == "s" and computer == "Paper") or (player == "p" and computer == "Rock") :

            # Update score
            score = score + 1
            print("You beat " + computer)
        
        # Computer wins
        elif (player == "p" and computer == "Scissors") or (player == "s" and computer == "Rock") or (player == "r" and computer == "Paper") :

            # Exit game
            winning = False

        # Tie
        elif (player == "p" and computer == "Paper") or (player == "r" and computer == "Rock") or (player == "s" and computer == "Scissors") :
            print("Tie!")
        
        # Invalid input
        else :
            print("That was invalid")

print("*** *** ***")
time.sleep(1)
print("Game over!")
time.sleep(1)

# Display results
print("Score >>> " + str(score) + " points")
time.sleep(1)

# Check high score
data = shelve.open('score.txt')
current_highest = data['highest_score']

# Update score.txt if new record set
if score > current_highest :
    print("\n*^* New Personal Best Unlocked *^*")
    time.sleep(1)
    print("         > " + str(score) + " points <")
    time.sleep(1)
    data['highest_score'] = score

# Otherwise, display current high score
else :
    print("\n ~ Current Best ~")
    print("   > " + str(current_highest) + " points <")
data.close()