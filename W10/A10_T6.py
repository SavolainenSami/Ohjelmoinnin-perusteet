########################################################
# Task A10_T6
# Developer Sami Savolainen
# Date 2025-12-11
########################################################

import time, copy
from typing import Callable


def readValues(values: list[int]) -> str:
    fname = input("Insert dataset filename: ")
    values.clear()
    try:
        with open(fname) as f:
            for line in f:
                line = line.strip()
                if line:
                    values.append(int(line))
    except:
        print("File not found.")
        return ""
    return fname


def bubbleSort(a: list[int]) -> list[int]:
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def quickSort(a: list[int]) -> list[int]:
    if len(a) <= 1:
        return a
    p = a[len(a) // 2]
    return (
        quickSort([x for x in a if x < p])
        + [x for x in a if x == p]
        + quickSort([x for x in a if x > p])
    )


def measure(alg: Callable, arr: list[int]) -> int:
    s = time.perf_counter_ns()
    alg(arr)
    return time.perf_counter_ns() - s


def main():
    values, results, dataset = [], [], ""
    print("Program starting.")

    while True:
        print(
            "\nOptions:\n1 - Read dataset values\n2 - Measure speeds\n3 - Save results\n0 - Exit"
        )
        choice = input("Your choice: ")

        if choice == "0":
            print("Exiting program.")
            break

        if choice == "1":
            dataset = readValues(values)

        elif choice == "2":
            if not values:
                print("No dataset loaded.")
                continue

            b = measure(sorted, copy.deepcopy(values))
            u = measure(bubbleSort, copy.deepcopy(values))
            q = measure(quickSort, copy.deepcopy(values))

            print(f"Measured speeds for dataset '{dataset}':")
            print(f" - Built-in sorted {b} ns")
            print(f" - Buble sort {u} ns")
            print(f" - Quick sort {q} ns")

            results = [
                f"Measured speeds for dataset '{dataset}':",
                f" - Built-in sorted {b} ns",
                f" - Buble sort {u} ns",
                f" - Quick sort {q} ns",
            ]

        elif choice == "3":
            if not results:
                print("No results to save.")
                continue
            fname = input("Insert results filename: ")
            with open(fname, "w") as f:
                f.write("\n".join(results))

        else:
            print("Invalid choice.")

    print("\nProgram ending.")


if __name__ == "__main__":
    main()
