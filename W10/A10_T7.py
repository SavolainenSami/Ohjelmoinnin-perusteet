########################################################
# Task A10_T7
# Developer Sami Savolainen
# Date 2025-12-11
########################################################

import random

random.seed(1234)


def layMines(PMineField: list[list[int]], PMines: int):
    rows = len(PMineField)
    cols = len(PMineField[0])

    placed = 0
    while placed < PMines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if PMineField[r][c] != 9:
            PMineField[r][c] = 9
            placed += 1


def calculateNearbys(PMineField: list[list[int]]) -> None:
    rows = len(PMineField)
    cols = len(PMineField[0])

    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] == 9:
                continue

            count = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if PMineField[nr][nc] == 9:
                        count += 1

            PMineField[r][c] = count


def generateMinefield(
    PMineField: list[list[int]], PRows: int, PCols: int, PMines: int
) -> None:
    PMineField.clear()

    for _ in range(PRows):
        PMineField.append([0 for _ in range(PCols)])

    layMines(PMineField, PMines)
    calculateNearbys(PMineField)


def main() -> None:
    print("Program starting.")
    board = []

    while True:
        print("Options:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board")
        print("3 - Save generated board")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "0":
            print("Exiting program.\n")
            break

        elif choice == "1":
            rows = int(input("Insert rows: "))
            cols = int(input("Insert columns: "))
            mines = int(input("Insert mines: "))
            generateMinefield(board, rows, cols, mines)

        elif choice == "2":
            for row in board:
                print(row)

        elif choice == "3":
            filename = input("Insert filename: ")
            with open(filename, "w") as f:
                for row in board:
                    f.write(",".join(map(str, row)) + "\n")

        else:
            print("Invalid choice.\n")

    print("Program ending.")


main()
