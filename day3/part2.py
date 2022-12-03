import sys


if __name__ == "__main__":
    priority = 0
    idx = 0
    lines = sys.stdin.readlines()
    
    for line in lines[::3]:
        line_1 = line.strip()
        line_2 = lines[idx+1].strip()
        line_3 = lines[idx+2].strip()

        common = ''.join(set(line_1).intersection(line_2, line_3))
        offset = 0
        if common.isupper():
            offset = 26

        priority += (ord(common.lower()) % 96) + offset
        idx += 3
    print(f"Total priority is {priority}")