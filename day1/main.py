import sys


if __name__ == "__main__":
    max_cal = -1
    running_cal = 0

    for line in sys.stdin:
        strip_line = line.strip()
        if strip_line == "":
            # sum and compare against max
            max_cal = running_cal if running_cal > max_cal else max_cal
            running_cal = 0
        else:
            running_cal += int(strip_line)
    
    print(f"Max Calories is {max_cal}")
