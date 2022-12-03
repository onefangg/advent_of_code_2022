import sys


if __name__ == "__main__":
    priority = 0

    for l in sys.stdin:
        line = l.strip()
        div = len(line) // 2
        compart_1, compart_2 = line[:div], line[div:]
        
        common = ''.join(set(compart_1).intersection(compart_2))
        offset = 0
        if common.isupper():
            offset = 26

        priority += (ord(common.lower()) % 96) + offset

    print(f"Total priority is {priority}")