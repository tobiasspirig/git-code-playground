import sys

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description = "Enter the name of the player.")
    parser.add_argument(
        "-n", "--name", metavar = "Name,", required = True, help = "The Player's Name."
    )
args = parser.parse_args()

game_count=0
wins = 0
def guess_number(name = "PlayerOne"):
    global game_count
    global wins
    from random import randint
    while True:
        choice_str = input(f"\n{name}, guess which number I am thinking of ... 1, 2, or 3: ")
        try:
            choice = int(choice_str)
            if choice in [1, 2, 3]:
                break
            else:
                print(f"Invalid key! {name}, please enter 1, 2, or 3.")
        except ValueError:
            print(f"Invalid input! {name}, please enter a number.")
       
    py_choice = randint(1,3)
    if choice == py_choice:
        print(f"\n{name}, that's right, you and Python both chose {choice}.")
        wins += 1
    else:
        print(f"\nSorry {name}, you chose {choice} and Python chose {py_choice}.")
    game_count +=1
    win_percentage = wins / game_count
    print (f"\nWin Percentage: {win_percentage:.1%}")
    while True:
        go_again=input(f"\n{name}, do you want to go again? Press y to go again and q to quit!")
        if go_again in "yY":
            return guess_number(name)
        elif go_again in "qQ":
            print(f"Bye {name}, thanks for playing.\n Final stats:\n Game count: {game_count}\nWins: {wins}\nLosses: {game_count-wins}\nWin Percentage: {win_percentage:.1%}")
            sys.exit()
        else:
            print ("Invalid key, please enter either y or q!")
guess_number(name = args.name)