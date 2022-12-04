import sys
import typing 

def get_min_max(range_str: str) -> typing.Tuple[int, int]:
    min_str, max_str = range_str.split("-")
    return int(min_str), int(max_str)


if __name__ == "__main__":
    pair_count = 0

    for l in sys.stdin:
        line = l.strip()
        elf_one, elf_two = line.split(",")

        elf_one_min, elf_one_max = get_min_max(elf_one)
        elf_two_min, elf_two_max = get_min_max(elf_two)

        if elf_one_min <= elf_two_min <= elf_one_max or \
            elf_one_min <= elf_two_max <= elf_one_max:
            pair_count += 1
        elif elf_two_min <= elf_one_min <= elf_two_max or \
            elf_two_min <= elf_one_max <= elf_two_max:
            pair_count += 1
    print(f"Pair count matches: {pair_count}")