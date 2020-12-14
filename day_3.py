

def get_input():
    input = []
    with open("day_3.txt") as f:
        for line in f:
            input.append(line.rstrip('\n'))
    return input

def traverse_slope(right=3, down=1):
    slope = get_input()
    row = 0
    col = 0
    tree = 0
    while row < len(slope) - 1:
        row += down
        col += right
        if col > len(slope[0]) - 1:
            col = col - len(slope[0])
        if slope[row][col] == '#':
            tree += 1
        if col == len(slope[0]) - 1:
            col = -1
    return tree

def traverse_many_slopes():
    slope1 = traverse_slope(1, 1)
    slope2 = traverse_slope(3, 1)
    slope3 = traverse_slope(5, 1)
    slope4 = traverse_slope(7, 1)
    slope5 = traverse_slope(1, 2)
    return slope1 * slope2 * slope3 * slope4 * slope5

if __name__ == '__main__':
    print(traverse_many_slopes())