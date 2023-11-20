import os

#local imports
import utils

class Highscore:
    def __init__(self, score_file):
        self.score_file = score_file

    def add_score(self, name, points, tot_time, g_wpm, n_wpm, w_precision, c_precision, mode):
        with open(self.score_file, "a+") as score:
            score.write(
                f"{name} {points} {tot_time} {g_wpm} {n_wpm} {w_precision} {c_precision} {mode}\n")

    def clear_scores(self):
        print("High scores cleared")
        with open(self.score_file, "w") as file:
            file.write("")

    def print_high_scores(self):
        scores = self.read_scores()
        if not scores:
            utils.print_empty()
            return

        sorted_scores = sorted(scores.items(), key=self.sorting_criteria, reverse=True)
        print("\033[1mThe best SwifTypers are:\033[0m")
        utils.print_high_score(sorted_scores)

    # Sorting key for high scores
    def sorting_criteria(self, item: dict):
        return item[1]['w_prec'] + item[1]['net_wpm'] + item[1]['mode']

    def read_scores(self):
        scores_dict = {}
        if os.path.exists(self.score_file) is False:
            return None
        with open(self.score_file, "r") as file:
            file.seek(0)
            scores = file.readlines()
            if not scores:
                return None
            scores_dict = self.scorestring_to_dict(scores, scores_dict)
        return scores_dict

    def scorestring_to_dict(self, scores, scores_dict):
        for score in scores:
            if len(score) > 1:
                name, tot_time, score, g_wpm, n_wpm, w_precision, c_precision, mode = score.split()
                scores_dict[name] = {
                    'time': round(float(tot_time), 2),
                    'score': score,
                    'gross_wpm': g_wpm,
                    'net_wpm': n_wpm,
                    'w_prec': w_precision,
                    'c_prec': c_precision,
                    'mode': mode}
        return scores_dict