import sys

def read_input(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    paper_rolls = dict()
    for i in range(len(lines)):
        shelf = []
        for j in range(len(lines[i])):
            if lines[i][j] == '@':
                shelf.append(j)
        paper_rolls[i] = shelf
    return len(lines), len(lines[0]), paper_rolls

def evaluate_position(i, j, paper_rolls, l_shelves):
    paper_rolls_count = 0
    shelf = paper_rolls[i]
    neighbors =  range(max(0, j-1), min(l_shelves, j+2))
    if i > 0:
        up = paper_rolls.get(i-1)
        paper_rolls_count += len([x for x in neighbors if x in up])
    if j > 0 and j - 1 in shelf:
        paper_rolls_count += 1
    if j < l_shelves - 1 and j + 1 in shelf:
        paper_rolls_count += 1
    if i < len(paper_rolls) - 1:
        down = paper_rolls.get(i+1)
        paper_rolls_count += len([x for x in neighbors if x in down])

    return paper_rolls_count < 4

def act_part2(nb_shelves, l_shelves, paper_rolls):
    to_be_removed = []
    for i in range(nb_shelves):
        for j in paper_rolls[i]:
            output = evaluate_position(i, j, paper_rolls, l_shelves)
            if output:
                to_be_removed.append((i, j))

    return to_be_removed

def act_part1(nb_shelves, l_shelves, paper_rolls):
    output = 0
    for i in range(nb_shelves):
        for j in paper_rolls[i]:
            output += evaluate_position(i, j, paper_rolls, l_shelves)

    return output

def replace_removed(to_be_removed, paper_rolls):
    for (i, j) in to_be_removed:
        paper_rolls[i] = [x for x in paper_rolls[i] if x != j]
    return paper_rolls

def main():
    arguments = sys.argv
    nb_shelves, l_shelves, file = read_input(arguments[1])
#    output = act_part1(nb_shelves, l_shelves, file)

    output = 0
    removed = 10
    while removed > 0:
        to_be_removed = act_part2(nb_shelves, l_shelves, file)
        removed = len(to_be_removed)
        output += removed
        file = replace_removed(to_be_removed, file)

    print(output)


if __name__ == '__main__':
    main()
