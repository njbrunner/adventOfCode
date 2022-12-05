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
        hands = line.split()
        opponent_hand = hands[0]
        my_hand = hands[1]
        total_score += calculate_score(opponent_hand, my_hand)

    print(f"Total Score: {total_score}")


def calculate_score(opponent_hand: str, my_hand: str):
    score = 0
    match my_hand:
        case "X":
            score += rock_score
            match opponent_hand:
                case "A":
                    score += draw_score
                case "B":
                    score += lose_score
                case "C":
                    score += win_score
        case "Y":
            score += paper_score
            match opponent_hand:
                case "A":
                    score += win_score
                case "B":
                    score += draw_score
                case "C":
                    score += lose_score
        case "Z":
            score += scissors_score
            match opponent_hand:
                case "A":
                    score += lose_score
                case "B":
                    score += win_score
                case "C":
                    score += draw_score
        case _:
            raise Exception(f"Invalid string for my_hand: {my_hand}")

    return score


if __name__ == "__main__":
    main()
