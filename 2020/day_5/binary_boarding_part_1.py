from typing import Tuple

with open('input.txt') as file:
    input = file.readlines()

puzzle_input = [line.strip() for line in input]

def get_selected_half(value: str, min: int, max: int, length: int) -> Tuple[int, int, int]:
    half_length = length/2
    if value == 'F' or value == 'L':
        return min, max - half_length, half_length
    return min + half_length, max, half_length

highest_seat_id = 0
for boarding_pass in puzzle_input:
    rows_min = 0
    rows_max = 127
    rows_length = 128
    columns_min = 0
    columns_max = 7
    columns_length = 8
    seat_row = 0
    seat_column = 0
    for value in boarding_pass:
        if value == 'F' or value == 'B':
            rows_min, rows_max, rows_length = get_selected_half(value, rows_min, rows_max, rows_length)
            # print(f'Row min: {rows_min} Row max: {rows_max} Rows length: {rows_length}')
        else:
            if boarding_pass[6] == 'F':
                seat_row = rows_min
            else:
                seat_row = rows_max
            columns_min, columns_max, columns_length = get_selected_half(value, columns_min, columns_max, columns_length)

    if boarding_pass[9] == 'L':
        seat_column = columns_min
    else:
        seat_column = columns_max

    print(f'Row: {seat_row} Column: {seat_column}')
    print(f'Seat ID: {seat_row * 8 + seat_column}')

    seat_id = seat_row * 8 + seat_column
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id

print(f'Highest Seat ID: {highest_seat_id}')
