import sys

def read_input(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    return lines

def parse_line(line):
    command = line[0]
    steps = line[1:]
    return command, int(steps)

def act_part1(current, command, steps, output):
    direction = 1 if command == "R" else -1
    current = (current + direction * int(steps)) % 100
    output += current == 0
    return current, output

def act_part2(start, command, steps, output):
    direction = 1 if command == "R" else -1
    current = (start + direction * steps) % 100
    output += int(steps / 100)
    rem = steps % 100
    if (start != 0 and ( current == 0
                         or (direction == 1 and start + rem > 100)
                         or (direction == -1 and start - rem < 0)
    )):
        output += 1
    return current, output

def main():
    arguments = sys.argv
    lines = read_input(arguments[1])
    start = 50
    output = 0
    for line in lines:
        command, steps = parse_line(line)
        # start, output = act_part1(current=start, command=command, steps=steps, output=output)
        start, output = act_part2(start=start, command=command, steps=steps, output=output)
    print(output)

if __name__ == '__main__':
    main()
