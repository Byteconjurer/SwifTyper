import os

def print_logo():
    """Prints the SwifTyper logo"""

    print("""\033[1m \033[1;34m
   ____       _ _________                 
  / __/    __(_) _/_  __/_ _____  ___ ____
 _\ \| |/|/ / / _/ / / / // / _ \/ -_) __/
/___/|__,__/_/_/  /_/  \_, / .__/\__/_/   
                      /___/_/          

      \033[1;35m    Elevate Your Typing, Surpass the Speed Barrier!   \033[0m
"""
          )
    

def press_to_continue():
    print("\nPress any key to continue...")
    input()

def clear():
    """Clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_empty():
    print("No scores yet")

def print_main_menu():
    
    print("Main Menu:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Time Attack")
    print("5. High Score")
    print("6. Quit")

def print_timeattack_menu():
    
    print("Time Attack")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Back")

def print_starting_message(mode, timeattack = False, set_time = 0):
    print(f"Starting {mode} mode...")
    if timeattack:
        print(f"You have {set_time} seconds to type as many words as you can!")
    print("Press a button to start.")
    input()
    clear()


def print_result(tot_time, stats, mode, gross_wpm, net_wpm, word_precision, char_precision):

    print(f"\nFinished!\nYour time was {round(tot_time, 2)} seconds on {mode} mode and you typed" \
        f" {stats['correct_words']}/{stats['word_count']} words correctly. You scored {stats['word_points']} " \
        f"word points!\nYou typed {stats['correct_chars']}/{stats['char_count']} characters correctly, "
        f"and you scored {stats['char_points']} character points!\n Your gross typing speed was "\
        f"{gross_wpm} wpm and your net speed was {net_wpm} wpm with a word precision of {word_precision}%\n" \
        f"and a character precision of {char_precision}%.\n")
    
def print_timeattack_result(stats, mode, set_time, gross_wpm, net_wpm, word_precision, char_precision):
        
    print(
    f"\nFinished!\nYou typed {stats['word_count']} words in {set_time} seconds on {mode} mode.\n" \
    f"You typed {stats['correct_words']}/{stats['word_count']} words correctly, and you scored" \
    f" {stats['word_points']} word points!\n"
    f"You typed {stats['correct_chars']}/{stats['char_count']} characters correctly, and you scored " \
    f"{stats['char_points']} character points!\nYour gross typing speed was {gross_wpm} wpm and your net speed " \
    f"was {net_wpm }wpm with a word precision of " \
    f"{word_precision}%\nand a character precision of {char_precision}%.\n")

def print_high_score(sorted_scores):

    for key, value in sorted_scores:
        print(f"{key:<20} {value['score']} word points{'':<5} {value['time']} seconds{'':<5} " \
              f"{value['net_wpm']} net wpm{'':<5} {value['w_prec']}% word precision{'':<5}  " \
              f"{value['c_prec']}% character precision{'':<5} on {modes(value['mode'])} mode")

def modes(mode):
    """Junction table for the modes"""

    mode_dict = {
        'EASY': 1,
        'MEDIUM': 4,
        'HARD': 8
    }
    dict_mode = {
        1: 'EASY',
        4: 'MEDIUM',
        8: 'HARD'
    }
    if mode not in mode_dict:
        return dict_mode[int(mode)]
    return mode_dict[mode]

def difficulty_select():
    print("1. Easy\n2. Medium\n3. Hard\n4. Back")
    while True:
        difficulty = input("Select a difficulty: ")
        if difficulty.isdigit() and int(difficulty) in [1, 2, 3, 4]:
            if difficulty == '2':
                return 4
            elif difficulty == '3':
                return 8
            return difficulty
        else:
            print("Not an option, try again.")

def input_name():
    name = input("\nPlease enter your name: ")
    while " " in name or name == "":
        if name == "":
            name = input("Name cannot be empty\n")
        if " " in name:
            name = input("No spaces allowed in name\n")
    return name

def time_select():
    while True:
        time = input("Select a time (seconds): ")
        if time.isdigit():
            return int(time)
        else:
            print("Please enter a valid number")
   