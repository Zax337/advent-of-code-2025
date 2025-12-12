import sys


def read_input(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    return lines


def find_all_indexes(line, num):
    result = []
    for i in range(len(line)):
        if line[i] == str(num):
            result.append(i)
    return result

def act_part1(banks):
    j1 = max(banks)
    j1_index = banks.index(j1)

    if j1_index == len(banks) - 2:
        j2 = j1
        j2_index = banks.index(j2)
        j1 = max(banks[:j2_index])
    else:
        j2 = max(banks[j1_index + 1:])
    return j1 + j2

def act_part2(line):
    bank = line.rstrip('\n')
    result = []
    while len(result) < 12 and len(bank) > 11 - len(result):
        search = bank[:-(11-len(result))] if len(result) < 11 else bank
        candidate = max(search)
        result.append(candidate)
        index = bank.index(candidate)
        bank = bank[index + 1:]

    if len(result) < 12:
        result.extend(bank[:-(12-len(result))])
    return ''.join(result)

def main():
    arguments = sys.argv
    lines = read_input(arguments[1])
    output = 0
    for line in lines:
        output += int(act_part2(line))
    print(output)

if __name__ == '__main__':
    main()
