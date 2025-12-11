########################################################
# Task A10_T4
# Developer Sami Savolainen
# Date 2025-12-11
########################################################


import sys
from A10_TLib import mergeSort


def readValues(filename: str) -> list[int]:
    values = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                values.append(int(line))
    return values


def displayValues(values: list[int]) -> str:
    return ", ".join(str(x) for x in values)


def main() -> None:
    print("Program starting.")

    if len(sys.argv) == 2:
        filename = sys.argv[1]
        print(f"The filename '{filename}' was passed via CLI.")
    else:
        filename = input("Insert filename: ")

    values = readValues(filename)
    print(f"Raw '{filename}' -> {displayValues(values)}")

    asc = values.copy()
    mergeSort(asc, True)
    print(f"Ascending '{filename}' -> {displayValues(asc)}")

    desc = values.copy()
    mergeSort(desc, False)
    print(f"Descending '{filename}' -> {displayValues(desc)}")


if __name__ == "__main__":
    main()
