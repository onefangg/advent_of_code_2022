import sys
from math import prod

if __name__ == "__main__":
    def is_visible(lst):
        if len(lst) == 1:
            return True

        base = lst[0]

        if base > max(lst[1:]):
            return True
        return False

    def num_visible(lst):
        if len(lst) == 1:
            return 0

        base = lst[0]
        num_trees = 0
        for tree in lst[1:]:
            num_trees+=1
            if tree >= base:
                break

        return num_trees
            

    map_grid = []

    for l in sys.stdin:
        line = l.strip()
        tree = list(line)
        map_grid.append([int(x) for x in tree])


    row_len = len(map_grid)
    col_len = len(map_grid[0])
    
    num_trees = 0
    max_scenic_score = -1
    for row_idx in range(row_len):
        for col_idx in range(col_len):

            left = [map_grid[row_idx][idx] for idx in range(col_idx, -1, -1)]
            right = [map_grid[row_idx][idx] for idx in range(col_idx, col_len)]
            up = [map_grid[idx][col_idx] for idx in range(row_idx, -1, -1)]
            down = [map_grid[idx][col_idx] for idx in range(row_idx, row_len)]

            is_viz = max(is_visible(left), is_visible(right),
                         is_visible(down), is_visible(up))

            if is_viz:
                num_trees+=1

            scenic_score = prod([num_visible(left), num_visible(right),
                                num_visible(down), num_visible(up)])
            max_scenic_score = scenic_score \
                 if scenic_score > max_scenic_score else max_scenic_score

    print(f"Number of Visible Trees: {num_trees}")
    print(f"Max Scenic Score: {max_scenic_score}")
