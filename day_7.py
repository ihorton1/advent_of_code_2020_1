from collections import defaultdict
def get_input():
    input = []
    with open("day_7.txt") as f:
        for line in f:
            input.append(line.rstrip('\n'))
    input.append('')
    return input

def process_rules():
    rules = get_input()
    #rules = ['vibrant salmon bags contain 1 vibrant gold bag, 2 wavy aqua bags, 1 dotted crimson bag.']
    rules_dict = {}
    for rule in rules:
        rule = rule[:-1].replace(' bags contain ', ', ').replace('no', '0 no').replace(' bags', '').replace(' bag', '').split(', ')
        sub_rule_list = []
        for sub_rule in range(1, len(rule)):
            sub_rule_list = sub_rule_list + (int(rule[sub_rule][0])*[rule[sub_rule][2:]])
        rules_dict[rule[0]] = sub_rule_list

    return rules_dict

def find_shing_gold_bags():
    rules = process_rules()
    result = defaultdict(int)
    queue = ['shiny gold']
    while queue:
        bag = queue[0]
        for key, value in rules.items():
            if bag in value:
                if result[key] == 0:
                    print(key)
                    result[key] += 1
                queue.append(key)
        queue = queue[1:]
    return sum(result.values())

def find_contained_bags(bag, rules):
    result = 0
    contained_bags = rules[bag]
    while len(contained_bags) > 0:
        result += 1
        current_bag = contained_bags[0]
        contained_bags = contained_bags + rules[current_bag]
        contained_bags = contained_bags[1:]
    return result

if __name__ == '__main__':
    print(find_contained_bags('shiny gold', process_rules()))