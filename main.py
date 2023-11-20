from swiftyper import Swiftyper
import utils


def Main():

    game = Swiftyper()

    utils.print_logo()
    print("Press a button to start.")
    input()

    while True:
        utils.clear()
        utils.print_main_menu()

        choice = input("\nPlease enter your choice: ")
        match choice:
            case '1':
                game.start_game("EASY")
            case '2':
                game.start_game("MEDIUM")
            case '3':
                game.start_game("HARD")
            case '4':
                utils.print_timeattack_menu()
                utils.clear()
                choice = utils.difficulty_select()
                time = utils.time_select()
                game.start_time_attack(utils.modes(choice), time)
            case '5':
                game.high_score.print_high_scores()
                print("\nTime Attack:")
                game.time_attack_score.print_high_scores()
                utils.press_to_continue()
            case '6':
                break


if __name__ == "__main__":
    Main()
else:
    print("Can only run from main.py")
    exit(1)
