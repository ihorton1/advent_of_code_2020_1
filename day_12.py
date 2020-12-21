def get_input():
    input = []
    with open("day_12.txt") as f:
        for line in f:
            line = line.rstrip('\n')
            input.append(line)
    return input

def format_input():
    directions = get_input()
    formatted_directions = []
    for direction in directions:
        formatted_directions.append((direction[0],int(direction[1:])))

    return formatted_directions

def rotate_ferry(current_direction, turn):
    compass = 'NESW'
    i = compass.index(current_direction)
    if turn[0] == 'R':
        oriented_compass = compass[i:] + compass[:i]
    else:
        oriented_compass = compass[i::-1] + compass[:i:-1]

    rotation = int(turn[1]/90) if int(turn[1]/90) < 4 else 0
    return oriented_compass[rotation]

def move_ferry_compass(position, distance):
    if distance[0] == 'N':
        position['y'] += distance[1]
    elif distance[0] == 'S':
        position['y'] -= distance[1]
    elif distance[0] == 'E':
        position['x'] += distance[1]
    else:
        position['x'] -= distance[1]
    return position

def navigate():
    directions = format_input()
    position = {
        'bearing': 'E',
        'x': 0,
        'y': 0
    }
    for direction in directions:
        if direction[0] in 'NESW':
            move_ferry_compass(position, direction)
        elif direction[0] in 'LR':
            position['bearing'] = rotate_ferry(position['bearing'], direction)
        else:
            move_ferry_compass(position, (position['bearing'], direction[1]))
    return abs(position['x']) + abs(position['y'])

def move_waypoint(position, distance):
    if distance[0] == 'N':
        position['w_y'] += distance[1]
    elif distance[0] == 'S':
        position['w_y'] -= distance[1]
    elif distance[0] == 'E':
        position['w_x'] += distance[1]
    else:
        position['w_x'] -= distance[1]
    return position

def rotate_waypoint(position, turn):
    compass = 'NESW'
    i = compass.index(position['bearing'])
    if turn[0] == 'R':
        oriented_compass = compass[i:] + compass[:i]
    else:
        oriented_compass = compass[i::-1] + compass[:i:-1]

    rotation = int(turn[1] / 90) if int(turn[1] / 90) < 4 else 0
    position['bearing'] = oriented_compass[rotation]
    if (turn[0]=='R' and rotation == 1) or (turn[0]=='L' and rotation == 3):
        y = -position['w_x']
        x = position['w_y']
    elif rotation == 2:
        y = -position['w_y']
        x = -position['w_x']
    elif (turn[0] == 'L' and rotation == 1) or (turn[0] == 'R' and rotation == 3):
        y = position['w_x']
        x = -position['w_y']

    position['w_y'] = y
    position['w_x'] = x

    return position

def move_ship(position, distance):
    position['s_y'] += distance[1]*position['w_y']
    position['s_x'] += distance[1]*position['w_x']
    return position

def navigate_2():
    directions = format_input()
    position = {
        'bearing': 'E',
        's_x': 0,
        's_y': 0,
        'w_x': 10,
        'w_y': 1
    }
    for direction in directions:
        if direction[0] in 'NESW':
            move_waypoint(position, direction)
        elif direction[0] in 'LR':
            rotate_waypoint(position, direction)
        else:
            move_ship(position, direction)
    return abs(position['s_x']) + abs(position['s_y'])

if __name__ == '__main__':
    print(navigate_2())