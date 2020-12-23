from collections import defaultdict
def get_input():
    input = []
    with open("day_13.txt") as f:
        input = []
        for line in f:
            input.append(line.rstrip('\n'))
        input1 = input[1].replace(',x', '').split(',')
        input = [int(input[0])]
        for item in input1:
            input.append(int(item))
    return input

def find_best_bus():
    buses = get_input()
    departure_ts = buses[0]
    min_wait = (departure_ts,0)
    for bus in buses[1:]:
        print(bus)
        new_wait = (departure_ts//bus+1)*bus-departure_ts
        print(new_wait)
        if new_wait < min_wait[0]:
            min_wait = (new_wait, bus)
    print(min_wait)
    return min_wait[0]*min_wait[1]

def get_input_2():
    with open("day_13.txt") as f:
        raw_input = []
        for line in f:
            raw_input.append(line.rstrip('\n'))
        raw_input = raw_input[1].split(',')
        input = []
        for x in raw_input:
            try:
                input.append(int(x))
            except:
                input.append(x)
    return input

def optimize_bus_departures(prior_buses_departure_period, prior_departure_time, next_bus, offset_seconds):
    period = prior_buses_departure_period*next_bus + 1
    prior_bus_arrivals = [x for x in range(prior_departure_time, period, prior_buses_departure_period)]
    for value in prior_bus_arrivals:
        if value > next_bus and (value+offset_seconds) % next_bus == 0:
            return value

def runner():
    buses = get_input_2()
    prior_buses_departure_period = buses[0]
    prior_departure_time = 0
    for i in range(1, len(buses)):
        if buses[i] != 'x':
            prior_departure_time = optimize_bus_departures(prior_buses_departure_period, prior_departure_time, buses[i], i)
            prior_buses_departure_period *= buses[i]
    return prior_departure_time


if __name__ == '__main__':
    print(runner())