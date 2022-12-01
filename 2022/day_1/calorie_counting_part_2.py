calories_carried = 0
elves = []


def main():
    file = open("input.text", "r")
    file_lines = file.readlines()

    for line in file_lines:
        if line.strip() == "":
            new_elf()
        else:
            global calories_carried
            calories_carried += int(line.strip())
    new_elf()

    print(get_value_of_maxes())


def new_elf():
    global calories_carried
    global elves
    elves.append(calories_carried)

    calories_carried = 0


def get_value_of_maxes():
    max_values = []
    for i in range(0, 3):
        index = elves.index(max(elves))
        max_values.append(elves.pop(index))
    return sum(max_values)


if __name__ == "__main__":
    main()
