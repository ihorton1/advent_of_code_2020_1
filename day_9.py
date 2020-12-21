def get_input():
    input = []
    with open("day_9.txt") as f:
        for line in f:
            input.append(int(line.rstrip('\n')))
    return input

def find_error():
    numbers = get_input()
    for i in range(25, len(numbers)):
        target = numbers[i]
        l, r = 0, 24
        temp_list = numbers[i - 25:i]
        temp_list.sort()
        while l < r:
            temp_sum = temp_list[l] + temp_list[r]
            if temp_sum > target:
                r -= 1
            elif temp_sum < target:
                l += 1
            else:
                break
        if l >= r:
            return target

def find_series_sum(target):
    numbers = get_input()
    l, r = 0, 2
    calc_sum = 0
    while calc_sum != target:
        calc_sum = sum(numbers[l:r])
        if calc_sum < target:
            r += 1
        elif calc_sum > target:
            l += 1
        else:
            return min(numbers[l:r]) + max(numbers[l:r])

if __name__ == '__main__':
    target = find_error()
    print(find_series_sum(target))