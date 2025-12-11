########################################################
# Task A10_T3
# Developer Sami Savolainen
# Date 2025-12-11
########################################################

import sys
from A10_TLib import readValues, displayValues, bubbleSort


def main() -> None:
    Values: list[int] = []
    Filename = ""

    print("Program starting.")

    if len(sys.argv) == 2:
        Filename = sys.argv[1]
        print(f"The filename '{Filename}' was passed via CLI.")
    else:
        Filename = input("Insert filename: ")

    readValues(Filename, Values)

    print(f"Raw '{Filename}' -> {displayValues(Values)}")

    asc = Values.copy()
    bubbleSort(asc, True)
    print(f"Ascending '{Filename}' -> {displayValues(asc)}")

    desc = Values.copy()
    bubbleSort(desc, False)
    print(f"Descending '{Filename}' -> {displayValues(desc)}")

    Values.clear()


if __name__ == "__main__":
    main()
