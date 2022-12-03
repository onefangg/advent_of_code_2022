import sys


if __name__ == "__main__":
    select_score_map = {
        "A": 1,  # rock
        "B": 2,  # paper
        "C": 3,  # scissors
    }
    win_map = {
        "A": "B",
        "B": "C",
        "C": "A"
    }

    lose_map = {
        "A": "C",
        "B": "A",
        "C": "B"
    }

    total_score = 0
    for l in sys.stdin:
        line = l.strip()
        opponent, outcome = line.split(" ")

        if outcome == "Y":
            # draw
            player = opponent
            total_score += select_score_map.get(player) + 3
        elif outcome == "X":
            # player loses
            player = lose_map.get(opponent)
            total_score += select_score_map.get(player) + 0
        elif outcome == "Z":
            # player wins
            player = win_map.get(opponent)
            total_score += select_score_map.get(player) + 6

    print(f"Total Score is {total_score}.")