from dice import dice

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

winning_score = 20
scoreboard = [0 for _ in range(player_number)]

while max(scoreboard) < winning_score:
    for player_list in range(player_number):
        print("It's player {} turn. Let's Go!".format(player_list + 1))
        print("Your current score is {}".format(scoreboard[player_list]))
        current_score = 0
        
        while True:
            player_prompt = input("Do you want to keep rolling or not: Type 'y' to continue - ")
            if player_prompt != "y":
                print("You ended your turn.\n")
                break

            dice_number = dice()

            if dice_number == 1:
                print("Oopsss! You just rolled {}. Your turn is done".format(dice_number))
                current_score = 0
                break
            else:
                print("You rolled {}".format(dice_number))
                current_score += dice_number

            print("Your total score in this turn is {}".format(current_score))

        scoreboard[player_list] += current_score
        print("Player {} total score in this game is {}\n".format(player_list + 1, scoreboard[player_list]))

game_result = max(scoreboard)
winning_player = scoreboard.index(game_result)

print("Congratulations player {} for winning the game of Pig. Your total score is {}".format(winning_player + 1, game_result))