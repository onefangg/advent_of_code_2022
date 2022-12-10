import sys


if __name__ == "__main__":
    input_text = sys.stdin.read()
    crates, instructions = input_text.split("\n\n")

    crates_lst = crates.split("\n")
    instruct_lst = instructions.strip().split("\n")
    
    crate_stacks, crate_order = crates_lst[:-1], crates_lst[-1]

    # indicates the index at which each item in `crate_stacks` are located
    crate_pos = [idx for idx, x in enumerate(crate_order) if x != ' ']

    curr_state = {int(c): [] for c in crate_order.split()}

    for idx in range(len(crate_stacks)-1, -1, -1):
        row = crate_stacks[idx]
        for item, pos in enumerate(crate_pos):
            if row[pos] == ' ':
                continue
            
            curr_state[item+1].append(row[pos])
    
    for instruct in instruct_lst:
        _, num_crate, _, source, _, target = instruct.split(" ")
        num_crate, source, target = int(num_crate), int(source), int(target)

        for i in range(num_crate):
            move = curr_state[source].pop()
            curr_state[target].append(move)
    
    result = ""
    for key, lst in curr_state.items():
        result += lst[-1]
    print(f"Result is {result}")


           
    