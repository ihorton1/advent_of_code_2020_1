from collections import defaultdict

def get_input():
    numbers = []
    with open("day_1.txt") as f:
        for line in f:
            numbers.append(int(line))
    return numbers

def find_2_2020():
    numbers = get_input()

    other_number = defaultdict(int)
    for n in numbers:
        if (2020 - n) in other_number:
            return n * (2020 - n)
        else:
            other_number[n] = 1

# Some day i will refactor this so its not o(n^3) time
def find_3_2020():
    numbers = get_input()

    for x in numbers:
        for y in numbers[1:]:
            for z in numbers[2:]:
                if x + y + z == 2020:
                    return x * y * z

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_input())
    print(find_2_2020())
    print(find_3_2020())
    find_3_2020()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
