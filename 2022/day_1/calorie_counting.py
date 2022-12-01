max_calories = 0
calories_carried = 0


def main():
    file = open("input.text", 'r')
    file_lines = file.readlines()

    for line in file_lines:
        if line.strip() == "":
            new_elf()
        else:
            global calories_carried
            calories_carried += int(line.strip())

    print(max_calories)


def new_elf():
    global max_calories
    global calories_carried
    if calories_carried > max_calories:
        max_calories = calories_carried
    calories_carried = 0


if __name__ == '__main__':
    main()
