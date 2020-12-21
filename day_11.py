import copy
def get_input():
    input = []
    with open("day_11.txt") as f:
        for line in f:
            line = line.rstrip('\n').replace('L', '#')
            input.append([x for x in line])
    return input

def pad_layout():
    seats = get_input()
    extra_row = ['.']*len(seats[0])
    seats.insert(0, extra_row)
    seats.append(extra_row)
    for row in range(len(seats)):
        seats[row].insert(0, '.')
        seats[row].append('.')

    return seats

def select_seat_patch(index, grid):
    seat_patch = [x[index[1]-1:index[1]+2] for x in grid[index[0]-1:index[0]+2]]

    return seat_patch

def check_seats(seat_patch):
    adjacent = 0
    for row in range(len(seat_patch)):
        for seat in range(len(seat_patch[row])):
            if seat_patch[row][seat] == '#' and (seat != 1 or row != 1):
                adjacent += 1

    return adjacent

def count_seats(seat_list):
    count = 0
    for seat in seat_list:
        if seat == '#':
            count += 1
    return count

def check_seats_two(index, grid):
    checker = [(1,0), (0,1), (-1,0), (0,-1), (1, -1), (1,1), (-1, 1), (-1, -1)]
    adjacent = 0
    for direction in checker:
        row = direction[0]
        col = direction[1]
        x = index[0]
        y = index[1]
        seat = '.'
        while seat == '.' and x > 0 and y > 0:
            x += row
            y += col
            try:
                seat = grid[x][y]
            except IndexError:
                break
        if seat == '#':
            adjacent += 1
    return adjacent

def iterate_over_grid():
    grid = pad_layout()
    new_grid = copy.deepcopy(grid)
    same_grid = False
    while not same_grid:
        for x in range(1, len(grid)-1):
            for y in range(1,len(grid[x])-1):
                if grid[x][y] != '.':
                    # patch = select_seat_patch((x, y), grid)
                    # action = check_seats(patch)
                    action = check_seats_two((x, y), grid)
                    if grid[x][y] == '#' and action >= 5:
                        new_grid[x][y] = 'L'
                    elif grid[x][y] == 'L' and action == 0:
                        new_grid[x][y] = '#'
        if str(grid) == str(new_grid):
            same_grid = True
        else:
            print(new_grid)
            grid = copy.deepcopy(new_grid)
    return count_seats(sum(new_grid, []))

if __name__ == '__main__':
    print(iterate_over_grid())