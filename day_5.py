import numpy as np
def get_input():
    input = []
    with open("day_5.txt") as f:
        for line in f:
            input.append(line.rstrip('\n'))
    return input

def decode_sequence(seat, row=True):
    if row:
        l_str_bound = 0
        r_str_bound = 7
        r = 127
        key = 'F'
    else:
        l_str_bound = 7
        r_str_bound = 10
        r = 7
        key = 'L'
    l = 0
    for i in range(l_str_bound, r_str_bound):
        mid = (l + r)//2
        if seat[i] == key:
            r = mid
        else:
            l = mid + 1
    if seat[i] == key:
        return l
    else:
        return r

def get_max_seat_id():
    seats = get_input()
    max_seat_id = 0
    for seat in seats:
        row = decode_sequence(seat, row=True)
        col = decode_sequence(seat, row=False)
        max_seat_id = max(max_seat_id, row*8+col)
    return max_seat_id

def create_plane():
    return np.zeros((128, 8))

def fill_plane():
    seats = get_input()
    plane = create_plane()
    for seat in seats:
        row = decode_sequence(seat, row=True)
        col = decode_sequence(seat, row=False)
        plane[row][col] = 1.0
    return plane

def find_seat():
    plane = fill_plane()
    for i in range(len(plane)-1):
        row_1 = sum(plane[i])
        row_2 = sum(plane[i + 1])
        row_3 = sum(plane[i + 2])
        if row_1 == row_3 and row_1 != row_2:
            return (i + 1)*8 + list(plane[i + 1]).index(0)

if __name__ == '__main__':
    print(find_seat())