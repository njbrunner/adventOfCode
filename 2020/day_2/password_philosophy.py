with open('input.txt') as file:
    input = file.readlines()

puzzle_input = [line.strip() for line in input]

# First Challenge
valid_passwords = 0

for item in puzzle_input:
    split_item = item.split()
    min = int(split_item[0].split('-')[0])
    max = int(split_item[0].split('-')[1])
    letter = split_item[1].replace(':', '')
    password = split_item[2]

    occurances = password.count(letter)
    if occurances >= min and occurances <= max:
        valid_passwords += 1

print(valid_passwords)

# Second Challenge
valid_passwords = 0

for item in puzzle_input:
    split_item = item.split()
    first_position = int(split_item[0].split('-')[0])
    second_position = int(split_item[0].split('-')[1])
    letter = split_item[1].replace(':', '')
    password = [char for char in split_item[2]]

    if password[first_position-1] == letter:
        if password[second_position-1] != letter:
            valid_passwords += 1
    elif password[second_position-1] == letter:
        valid_passwords += 1

print(valid_passwords)
