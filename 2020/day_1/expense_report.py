with open('input.txt') as file:
    input = file.readlines()

puzzle_input = [int(line.strip()) for line in input]

for i in range(0, len(puzzle_input)):
    for j in range(i+1, len(puzzle_input)):
        for k in range(j+1, len(puzzle_input)):
            if (puzzle_input[i] + puzzle_input[j] + puzzle_input[k] == 2020):
                print(f'Answer: {puzzle_input[i]*puzzle_input[j]*puzzle_input[k]}')
