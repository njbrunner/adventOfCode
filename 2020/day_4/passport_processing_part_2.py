import re

puzzle_input = []
passport_object = {}
with open('input.txt') as file:
    for line in file:
        if line == '\n':
            puzzle_input.append(passport_object)
            passport_object = {}
        else:
            for key_value_pair in line.split(' '):
                passport_object[key_value_pair.split(':')[0]] = key_value_pair.split(':')[1].strip()
    if len(passport_object) is not None:
        puzzle_input.append(passport_object)

def is_valid(passport_value, validation: str) -> bool:
    """Checks value against validation.
    :param passport_value: The value to check.
    :param validation: The validation to perform.
    :return: Boolean determining if teh value is valid.
    """
    if re.match(validation, passport_value):
        return True
    return False

key_validation_pairs = {
    'byr': '^(19[2-9]\d|200[0-2])$',
    'iyr': '^(201[0-9]|2020)$',
    'eyr': '^(202[0-9]|2030)$',
    'hgt': '^(1[5-8]\dcm|19[0-3]cm|59in|6\din|7[0-6]in)$',
    'hcl': '^(#[0-9a-f]{6})$',
    'ecl': '^(amb|blu|brn|gry|grn|hzl|oth)$',
    'pid': '^([0-9]{9})$'
}

valid_passports = 0
for passport in puzzle_input:
    valid = True
    for key, validation in key_validation_pairs.items():
        if not key in passport:
            valid = False
        elif not is_valid(passport[key], validation):
            valid = False
    if valid:
        valid_passports += 1

print(valid_passports)
