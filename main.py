game_title = """

,--------.,--.          ,--------.                 ,--------.              
'--.  .--'`--' ,---.    '--.  .--',--,--. ,---.    '--.  .--',---.  ,---.  
   |  |   ,--.| .--'       |  |  ' ,-.  || .--'       |  |  | .-. || .-. : 
   |  |   |  |\ `--.       |  |  \ '-'  |\ `--.       |  |  ' '-' '\   --. 
   `--'   `--' `---'       `--'   `--`--' `---'       `--'   `---'  `----' 
                                                                           """

game_slots = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def draw_board():
    return f"""
      A | B | C
    1 {game_slots[0][0]} | {game_slots[0][1]} | {game_slots[0][2]}
      ----------
    2 {game_slots[1][0]} | {game_slots[1][1]} | {game_slots[1][2]}
      ----------
    3 {game_slots[2][0]} | {game_slots[2][1]} | {game_slots[2][2]}
    """


winning_slots = [
    [("1", "a"), ("1", "b"), ("1", "c")],
    [("2", "a"), ("2", "b"), ("2", "c")],
    [("3", "a"), ("3", "b"), ("3", "c")],
    [("1", "a"), ("2", "a"), ("3", "a")],
    [("1", "b"), ("2", "b"), ("3", "b")],
    [("1", "c"), ("2", "c"), ("3", "c")],
    [("1", "a"), ("2", "b"), ("3", "c")],
    [("3", "a"), ("2", "b"), ("1", "c")],
]

PLAYER_1_TOKEN = "X"
PLAYER_2_TOKEN = "0"

# Game starts

print(game_title)

print(draw_board())

print(f"Player 1: '{PLAYER_1_TOKEN}'; Player 2: '{PLAYER_2_TOKEN}'")
print("To select the location on your turn, type its address as 'row''column'; for example: '1a' or '2b'")

# Game is staged at this point. Need to create turns and player token placement.

current_game_data = [
    ["Player 1", PLAYER_1_TOKEN, []],
    ["Player 2", PLAYER_2_TOKEN, []]
]
# 9 rounds and the game is finished by default
current_round = 0.0

end_game = False

while not end_game:
    # determine which player is in play
    if current_round % 1 == 0.0:
        current_player = current_game_data[0]
    else:
        current_player = current_game_data[1]

    valid_choice = False
    while not valid_choice:
        player_choice = input(f"{current_player[0]}, make your selection: ").lower()
        if len(player_choice) == 2:
            location_of_interest = list(player_choice)

            if location_of_interest[0] in ["1", "2", "3"] and location_of_interest[1] in ["a", "b", "c"]:

                # translate column letter to row index
                if location_of_interest[1] == "a":
                    location_of_interest[1] = 0
                elif location_of_interest[1] == "b":
                    location_of_interest[1] = 1
                else:
                    location_of_interest[1] = 2

                # check if location is empty
                if game_slots[int(location_of_interest[0])-1][location_of_interest[1]] == " ":
                    game_slots[int(location_of_interest[0])-1][location_of_interest[1]] = current_player[1]

                    # add players choice to their list of choices
                    current_player[2].append(tuple(player_choice))
                    # show updated game board
                    print(draw_board())
                    valid_choice = True
                else:
                    print("That slot has been taken.")

            else:
                print("Choice is not valid.")
        else:
            print("Your input must be 2 characters long.")

    # determine winning play
    for winning_hand in winning_slots:
        winner = all(slot in current_player[2] for slot in winning_hand)
        if winner:
            print(f"{current_player[0]}, you are the winner!")
            end_game = True

    current_round += 0.5
    if current_round == 4.5 and not end_game:
        print("Game tied!")
        end_game = True




