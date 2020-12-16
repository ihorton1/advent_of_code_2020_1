from collections import defaultdict
def get_input():
    input = []
    with open("day_8.txt") as f:
        for line in f:
            input.append(line.rstrip('\n'))
    return input

def process_rules():
    rules = get_input()
    processed_rules = []
    for rule in rules:
        current_rule = []
        current_rule.append(rule[:3])
        current_rule.append(rule[4])
        current_rule.append(rule[5:])
        processed_rules.append(current_rule)
    return processed_rules

def find_loop(rules):
    rule_tracker = defaultdict(int)
    i = 0
    acc = 0
    while rule_tracker[i] == 0 and i < len(rules):
        rule_tracker[i] += 1
        if rules[i][0] == 'nop':
            i += 1
        elif rules[i][0] == 'acc':
            if rules[i][1] == '+':
                acc += int(rules[i][2])
            else:
                acc -= int(rules[i][2])
            i += 1
        elif rules[i][0] == 'jmp':
            if rules[i][1] == '+':
                i += int(rules[i][2])
            else:
                i -= int(rules[i][2])
    return acc, i

def find_change():
    rules = process_rules()
    i = 0
    x = 0
    while i < len(rules) and x < len(rules):
        loop_rules = process_rules()
        if loop_rules[x][0] == 'jmp':
            loop_rules[x][0] = 'nop'
        acc, i = find_loop(loop_rules)
        x += 1
    return acc

if __name__ == '__main__':
    print(find_change())