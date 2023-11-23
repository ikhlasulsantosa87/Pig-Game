from dice import dice # Import the dice() function that we created

# A loop that asking for how many players will play the game. If it 2 or less than equal to 4, the game proceeds and the loop breaks.
while True:
    try:
        player_number = int(input("How many players that want to play the game of Pig: "))
        if 2 <= player_number <= 4:
            print("{} players registered! Enjoy the game.\n".format(player_number))
            break
        else:
            print("This game only for 2 to 4 people! Try Again!")
    except ValueError:
        print("Invalid Input! Try Again!")

# Asking for the registered player their name and welcomes them
player_names = []

for _ in range(player_number):
    username = input("Enter your name: ")
    player_names.append(username)

print(f"Welcome {', '.join(player_names)}\n")

winning_score = 20 # The winning score for the game
scoreboard = [0 for _ in range(len(player_names))] # To store each player score and keep tracks it throughout the game

# If the winning score is not reach by either player, the game still on
while max(scoreboard) < winning_score:

    # Simulating of each player turn in the game
    for player_list in range(len(player_names)):
        print("It's {} turn. Let's Go!".format(player_names[player_list]))
        print("Your current score is {}".format(scoreboard[player_list]))
        current_score = 0
        
        # Ask the user for confirmation whether they want to continue with their turn or stop.
        while True:
            player_prompt = input("Do you want to keep rolling or not: Type 'y' to continue - ")
            if player_prompt != "y":
                print("You ended your turn.\n")
                break

            # Show the number of the dice that player of that turn rolled.    
            dice_number = dice()

            # Check if the number showed by the dice. If the player gets 1, all of their score in that turn is reset to 0 and if it is not it adds to their scoreboard.
            if dice_number == 1:
                print("Oopsss! You just rolled {}. Your turn is done".format(dice_number))
                current_score = 0
                break
            else:
                print("You rolled {}".format(dice_number))
                current_score += dice_number

            print("Your total score in this turn is {}".format(current_score))
        # Add the player score for that turn into the scoreboard to keep track.
        scoreboard[player_list] += current_score
        print("{} total score in this game is {}\n".format(player_names[player_list], scoreboard[player_list]))

# Determining who is the winner of the game
game_result = max(scoreboard)
winning_player = scoreboard.index(game_result)

# Display the winner
print("Congratulations {} for winning the game of Pig. Your total score is {}".format(player_names[winning_player], game_result))