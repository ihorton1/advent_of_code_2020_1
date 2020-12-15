from collections import defaultdict

def get_input():
    input = []
    with open("day_6.txt") as f:
        for line in f:
            input.append(line.rstrip('\n'))
    input.append('')
    return input

def count_plane_unique():
    #groups = get_input()
    groups = ['edmzkxfoprcnhijtyvl', 'adxntojykfcvzermplh', '']
    group_tally_dict = defaultdict(int)
    total = 0
    for group in groups:
        if group == '':
            total += sum(group_tally_dict.values())
            group_tally_dict = defaultdict(int)
            continue
        for q in group:
            if group_tally_dict[q] == 0:
                group_tally_dict[q] += 1
    print(total)

def count_plane_same():
    groups = get_input()
    group_tally_dict = defaultdict(int)
    total = 0
    members = 0
    for group in groups:
        members += 1
        if group == '':
            for key, value in group_tally_dict.items():
                if value == members - 1:
                    total += 1
            group_tally_dict = defaultdict(int)
            members = 0
            continue
        for q in group:
            group_tally_dict[q] += 1
    print(total)

if __name__ == '__main__':
    count_plane_same()