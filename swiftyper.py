"""SwifTyper is a typing game that allows you to test your typing speed and accuracy."""

import random
import time

#local imports
import gamestate
from highscore import Highscore
import animals
import utils
from texts import Texts

class Swiftyper:
    def __init__(self):
        self.high_score = Highscore("score.txt")
        self.time_attack_score = Highscore("timeattack_score.txt")


    def start_game(self, mode: str):
        """Starts the game with the given mode"""

        utils.clear()
        state = gamestate.GameState()

        utils.print_starting_message(mode, timeattack = False, set_time = 0)

        tot_time = 0
        random_text = Texts.get_random_text(mode)
        lines = random_text.split('\n')
        for line in lines:
            print(line, end='')
            typetime, inp = self.time_input()
            tot_time += typetime
            state.stats.update(self.score_words_chars(line, inp, state, timeattack = False))
            utils.clear()

        gross_wpm, net_wpm, word_precision, char_precision = self.calc_speed_precision(state.stats, tot_time)

        utils.print_result(tot_time, state.stats, mode, gross_wpm, net_wpm, word_precision, char_precision)
        animals.assign_animal(gross_wpm)

        if (char_precision) != 100:
            self.print_misspelled_chars(state.chars_dict)

        self.high_score.add_score(
                name = utils.input_name(),
                points = state.stats['word_points'], 
                tot_time = round(tot_time), 
                g_wpm = gross_wpm, 
                n_wpm = net_wpm,
                w_precision = word_precision, 
                c_precision = char_precision, 
                mode = utils.modes(mode)
        )
        utils.press_to_continue()


    def start_time_attack(self, mode: str, set_time: int):
        """Starts the time attack mode with the given mode and set time"""
        
        state = gamestate.GameState()
        utils.print_starting_message(mode, timeattack = True, set_time = set_time)
        random_text = Texts.get_random_text(mode)
        lines = random_text.split('\n')
        word_list = [word for line in lines for word in line.split()]

        time_count = 0
        rand = random.randint(0, len(word_list)-1)
        while time_count <= set_time:
            word = word_list[rand]
            print(word)
            typetime, inp = self.time_input()
            time_count += typetime
            state.stats.update(self.score_words_chars(word, inp, state, timeattack = True))
            utils.clear()
            rand = random.randint(0, len(word_list)-1)

        gross_wpm, net_wpm, word_precision, char_precision = self.calc_speed_precision(state.stats, time_count)

        utils.print_timeattack_result(state.stats, mode, set_time, gross_wpm, net_wpm, word_precision, char_precision)
        animals.assign_animal(gross_wpm)

        if (char_precision) != 100:
            self.print_misspelled_chars(state.chars_dict)

        self.time_attack_score.add_score(
                name = utils.input_name(),
                points = state.stats['word_points'], 
                tot_time = round(time_count), 
                g_wpm = gross_wpm, 
                n_wpm = net_wpm,
                w_precision = word_precision, 
                c_precision = char_precision, 
                mode = utils.modes(mode),   
                )
        utils.press_to_continue()

    def calc_speed_precision(self, stats: dict, tot_time: float):
        """Calculates the speed and precision of the user"""
        SEC_PER_MIN = 60
        gross_wpm = round(stats['inp_word_count']*SEC_PER_MIN/tot_time, 2)
        net_wpm = round(stats['correct_words']*SEC_PER_MIN/tot_time, 2)
        word_precision = round(stats['correct_words']/stats['word_count'], 2)*100
        char_precision = round(stats['correct_chars']/stats['char_count'], 2)*100

        if word_precision < 0:
            word_precision = 0

        return gross_wpm, net_wpm, word_precision, char_precision


    def score_words_chars(self, line: str, inp: str, state=gamestate.GameState(), timeattack=False):
        """Evaluates the words and characters typed by the user and returns the stats"""

        #Called iteratively on line 141.
        def update_stats(word, inp_word):
            nonlocal state
            if inp_word == word:
                state.stats['correct_words'] += 1
                state.stats['word_points'] += 1
            else:
                state.stats['word_points'] -= 1

            for wd, in_wd in zip(word, inp_word):
                state.chars_dict[wd] = state.chars_dict.get(wd, 0)
                if in_wd == wd:
                    state.stats['correct_chars'] += 1
                    state.stats['char_points'] += 1
                else:
                    state.stats['char_points'] -= 1
                    state.chars_dict[wd] += 1

        if timeattack:
            words = [line]
            inp_words = [inp]
            state.stats['char_count'] += len(words[0])
            state.stats['inp_char_count'] += len(inp_words[0])
            state.stats['word_count'] += len(words)
            state.stats['inp_word_count'] += len(inp_words)
        else:
            words = line.split()
            inp_words = inp.split()
            state.stats['word_count'] += len(words)
            state.stats['inp_word_count'] += len(inp_words)
            state.stats['char_count'] += sum(len(word) for word in words)
            state.stats['inp_char_count'] += sum(len(word) for word in inp_words)



        for word, inp_word in zip(words, inp_words):
            update_stats(word, inp_word)

        state.stats['char_points'] -= abs(state.stats['inp_char_count'] - state.stats['char_count'])
        state.stats['word_points'] -= abs(state.stats['word_count'] - state.stats['inp_word_count'])

        return state.stats

    def print_misspelled_chars(self, c_dict: dict):
        """Prints the misspelled characters"""

        print("Misspelled characters:\n")
        keys = []
        values = []
        for key, value in dict(sorted(c_dict.items(), key=lambda item: item[1], reverse=True)).items():
            if value > 0:
                keys.append(key)
                values.append(value)
        print(" ".join(map(str, keys)))
        print(" ".join(map(str, values)))

    def time_input(self):
        """Returns the time taken to type the input and the input itself"""

        start_time = time.time()
        inp = input("\n> ")
        end_time = time.time()
        elapsed_time = end_time - start_time
        return elapsed_time, inp











