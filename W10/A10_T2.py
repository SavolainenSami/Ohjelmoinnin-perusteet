########################################################
# Task A10_T2
# Developer Sami Savolainen
# Date 2025-12-11
########################################################

import sys


def readValues(PFilename: str, PValues: list[int]) -> None:
    try:
        with open(PFilename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        PValues.append(int(line))
                    except ValueError:
                        print("Error: File contains non-integer data.")
                        sys.exit()
    except FileNotFoundError:
        print("File not found.")
        sys.exit()
    return None


def sumOfValues(PValues: list[int]) -> int:
    return sum(PValues)


def productOfValues(PValues: list[int]) -> int:
    product = 1
    for num in PValues:
        product *= num
    return product


def main() -> None:
    Values: list[int] = []

    print("Program starting.")

    filename = input("Insert filename: ")

    readValues(filename, Values)

    total = sumOfValues(Values)

    product = productOfValues(Values)

    print("# --- Sum of numbers --- #")
    print(total)
    print("# --- Sum of numbers --- #")

    print("# --- Product of numbers --- #")
    print(product)
    print("# --- Product of numbers --- #")

    Values.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
