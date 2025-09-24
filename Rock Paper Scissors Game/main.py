# Rock Paper Scissors Game

# Ask the player to pick rock, paper or scissors.
# Have the computer chose its move.
# Compare the choices and decide who wins.
# Print the results.
# Subgoals:

# Give the player the option to play again.
# Keep a record of the score (e.g. Player: 3 / Computer: 6).


import random

global player_score
global computer_score

legend = {1: "rock", 2: "paper", 3: "scissors"}


def hand_string_to_int(hand: str) -> int:
    try:
        if int(hand) > 0 and int(hand) < 4:
            return int(hand)
    except:
        return None


def get_player_hand() -> int:
    player_hand = input(
        '1. Rock | 2. Paper | 3. Scissors\nEnter your option and press enter to submit: ')
    if player_hand == "quit":
        quit()
    player_hand = hand_string_to_int(player_hand)
    if player_hand != None:
        return player_hand
    else:
        print('Please enter a valid number (1 - 3) or type "quit" to quit.')
        get_player_hand()


def get_computer_hand() -> int:
    options = [1, 2, 3]
    return random.choice(options)


def compare_hands(p: int, c: int):
    global player_score, computer_score
    if (p == 1 and c == 3) or (p == 2 and c == 1) or (p == 3 and c == 2):
        player_score += 1
    else:
        computer_score += 1
    return


def main_loop():
    print(
        f'Player score is {player_score}\nComputer score is {computer_score}\n')
    while player_score < 3 and computer_score < 3:

        player_hand = get_player_hand()
        computer_hand = get_computer_hand()

        print(f'\nPlayer plays {legend[player_hand]}')
        print(f'Computer plays {legend[computer_hand]}\n')

        if computer_hand != player_hand:
            compare_hands(player_hand, computer_hand)

        else:
            print("Draw!\n")
            continue
        print(
            f'Player score is {player_score}\nComputer score is {computer_score}\n')
    if player_score > computer_score:
        print("Player wins!")
    else:
        print("Computer wins!")


while __name__ == "__main__":
    print(f'Welcome to Rock Paper Scissors!\nThe goal is to win 3 hands.\nType "quit" and press enter at any time to quit.\n')
    player_score = int(0)
    computer_score = int(0)
    main_loop()

    play_again = input("Do you want to play again? (Y/N)")
    if play_again.lower() == "y":
        continue
    else:
        break
