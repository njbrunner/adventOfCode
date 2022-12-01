puzzle_input = []
passport_array = []
with open('input.txt') as file:
    for line in file:
        if line == '\n':
            puzzle_input.append(passport_array)
            passport_array = []
        else:
            for key_value_pair in line.split(' '):
                passport_array.append(key_value_pair.strip())
    if len(passport_array) is not None:
        puzzle_input.append(passport_array)

key_only_array = []
for item in puzzle_input:
    key_only_array.append([index.split(':')[0] for index in item])

valid_passports = 0
required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in key_only_array:
    missing_key = False
    for key in required_keys:
        if key not in passport:
            missing_key = True

    if not missing_key:
        valid_passports += 1

print(valid_passports)
