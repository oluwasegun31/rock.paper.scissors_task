import random

while True:
    game_rules = 'Options\n"R" for rock,\n"P" for paper,\n"S" for scissors.'
    print(game_rules)

    player_select = input('Select one option ["R", "P" or "S"] : ')
    player_select_lower = player_select.lower()
    if player_select_lower == "r":
        player_choice = 'Rock'
    elif player_select_lower == "p":
        player_choice = 'Paper'
    elif player_select_lower == "s":
        player_choice = 'Scissors'
    else:
        print("Invalid Option Selected!\n PLEASE TRY AGAIN")
        continue

    game = ["Rock", "Paper", "Scissors"]

    computer_select = random.choice(game)
    print(
        f"You played ({player_choice}) : Computer played ({computer_select})")
    if player_choice == computer_select:
        print(f'Both Selected "{player_select}", TIE GAME!!!')
        continue
    elif player_choice == 'Rock':
        if computer_select == 'Scissors':
            print("CONGRATS YOU WIN!!!")
            break
        if computer_select == 'Paper':
            print("OH NO COMPUTER WINS!!!")
            break

    elif player_choice == 'Paper':
        if computer_select == 'Rock':
            print("CONGRATS YOU WIN!!!")
            break
        if computer_select == 'Scissors':
            print("OH NO COMPUTER WINS!!!")
            break

    elif player_choice == 'Scissors':
        if computer_select == 'Paper':
            print("CONGRATS YOU WIN!!!")
            break
        if computer_select == 'Rock':
            print("OH NO COMPUTER WINS!!!")
            break
    else:
        continue
