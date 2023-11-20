class GameState:
    def __init__(self):
        self.chars_dict = {}
        self.stats = {
            'word_points': 0,
            'char_points': 0,
            'correct_chars': 0,
            'correct_words': 0,
            'char_count': 0,
            'inp_char_count': 0,
            'word_count': 0,
            'inp_word_count': 0
        }