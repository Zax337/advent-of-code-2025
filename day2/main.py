import sys

def read_input(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    return lines

def parse_file(file):
    lines = file[0].split(',')
    return lines


def check_pattern_part1(num):
    l = len(num)
    if l % 2 != 0:
        return 0

    half_l = int(l/2)
    return num if num[0:half_l] == num[half_l:] else 0

def act_part1(bound_min, bound_max):
    invalid_ids = []
    for num in range(int(bound_min), int(bound_max)+1):
        if check_pattern_part1(str(num)):
            invalid_ids.append(num)
    return sum(invalid_ids)


def find_all_candidates(string, char):
    result = []
    half_l = len(string) / 2
    for i in range(int(half_l) + 1):
        if string[i] == char:
            result.append(i)
    return result[1:]

def check_candidate(num, candidate):
    l = len(num)
    if l % candidate != 0:
        return 0
    pattern_l = int(candidate)
    pattern_rep = int(l/candidate)
    for i in range(pattern_rep):
        if num[0:pattern_l] != num[i*pattern_l:(i+1)*pattern_l]:
            return 0
    return num

def check_pattern_part2(num):
    candidates = find_all_candidates(num, num[0])
    if len(candidates) == 0:
        return 0
    for candidate in reversed(candidates):
        if check_candidate(num, candidate):
            return num
    return 0

def act_part2(bound_min, bound_max):
    invalid_ids = []
    for num in range(int(bound_min), int(bound_max)+1):
        if check_pattern_part2(str(num)):
            invalid_ids.append(num)
    return sum(invalid_ids)


def main():
    arguments = sys.argv
    file = read_input(arguments[1])
    lines = parse_file(file)
    output = 0
    for line in lines:
        bounds = line.split('-')
        # output += act_part1(bounds[0], bounds[1])
        output += act_part2(bounds[0], bounds[1])

    print(output)


if __name__ == '__main__':
    main()
