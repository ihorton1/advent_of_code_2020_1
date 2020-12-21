from collections import defaultdict
def get_input():
    input = []
    with open("day_10.txt") as f:
        for line in f:
            input.append(int(line.rstrip('\n')))
    return input

def check_adapters():
    adapters = get_input()
    adapters.append(0)
    adapters.sort()
    differences = defaultdict(int)
    for i in range(1,len(adapters)):
        difference = adapters[i] - adapters[i-1]
        differences[difference] += 1
    differences[3] += 1
    return differences[1] * differences[3]

def check_all_combos():
    adapters = get_input()
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1]+3)
    print(adapters)
    memo = {adapters[0]: 1, adapters[1]: 1, adapters[2]: 2}
    for i in range(3,len(adapters)):
        combos = memo[adapters[i - 1]]
        if adapters[i] - adapters[i-3] <= 3:
            combos += memo[adapters[i-3]] + memo[adapters[i-2]]
        elif adapters[i] - adapters[i-2] <= 3:
            combos += memo[adapters[i - 2]]
        memo[adapters[i]] = combos
    print(memo)
    return memo[adapters[-1]]



if __name__ == '__main__':
    print(check_all_combos())