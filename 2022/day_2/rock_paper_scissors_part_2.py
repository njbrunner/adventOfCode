rock_score = 1
paper_score = 2
scissors_score = 3

lose_score = 0
draw_score = 3
win_score = 6


def main():
    file = open("input.txt", "r")
    file_lines = file.readlines()

    total_score = 0

    for line in file_lines:
        line_input = line.split()
        opponent_hand = line_input[0]
        outcome = line_input[1]
        total_score += calculate_score(opponent_hand, outcome)

    print(f"Total Score: {total_score}")


def calculate_score(opponent_hand: str, outcome: str):
    score = 0
    match opponent_hand:
        case "A":
            match outcome:
                case "X":
                    score += lose_score + scissors_score
                case "Y":
                    score += draw_score + rock_score
                case "Z":
                    score += win_score + paper_score
        case "B":
            match outcome:
                case "X":
                    score += lose_score + rock_score
                case "Y":
                    score += draw_score + paper_score
                case "Z":
                    score += win_score + scissors_score
        case "C":
            match outcome:
                case "X":
                    score += lose_score + paper_score
                case "Y":
                    score += draw_score + scissors_score
                case "Z":
                    score += win_score + rock_score
        case _:
            raise Exception(f"Invalid string for opponent_hand: {opponent_hand}")

    return score


if __name__ == "__main__":
    main()
