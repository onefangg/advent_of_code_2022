import sys


if __name__ == "__main__":
    """
    x, a = rock
    y, b = paper
    z, c = scissors
    """
    score_mapping = {
        "A Y": 6 + 2,
        "A X": 3 + 1,
        "A Z": 0 + 3,
        "B Y": 3 + 2,
        "B X": 0 + 1,
        "B Z": 6 + 3,
        "C Y": 0 + 2,
        "C X": 6 + 1,
        "C Z": 3 + 3,
    }
    
    total_score = 0
    for l in sys.stdin:
        line = l.strip()
        total_score += score_mapping.get(line)
    print(f"Total Score is {total_score}.")