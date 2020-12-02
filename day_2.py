import numpy as np

def get_input():
    numbers = []
    with open("day_2.txt") as f:
        for line in f:
            numbers.append(line.rstrip('\n'))
    return numbers

def process_passwords(password):
    password = password.split(' ')
    password[0] = list(map(int, password[0].split('-')))
    password[1] = password[1].rstrip(':')
    return password

def check_passwords_1(password):
    char_count = password[2].count(password[1])
    if char_count >= password[0][0] and char_count <= password[0][1]:
        return True
    return False

def check_passwords_2(password):
    first_occurance = password[2][password[0][0]-1]
    second_occurance = password[2][password[0][1]-1]
    if first_occurance == password[1] and second_occurance != password[1]:
        return True
    elif second_occurance == password[1] and first_occurance != password[1]:
        return True
    else:
        return False

def validate_passwords():
    passwords = get_input()
    passwords = [process_passwords(x) for x in passwords]
    validation_1 = [check_passwords_1(x) for x in passwords]
    validation_2 = [check_passwords_2(x) for x in passwords]
    print(validation_1.count(True))
    print(validation_2.count(True))


if __name__ == '__main__':
    validate_passwords()