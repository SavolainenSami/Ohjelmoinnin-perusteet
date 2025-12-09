########################################################
# Task A9_T3
# Developer Sami Savolainen
# Date 2025-12-09
########################################################

import sys


def main():
    print("Program starting.")

    filename = input("Insert filename: ")

    try:
        with open(filename, "r") as f:
            content = f.read()
    except:
        print(f'Couldn\'t read file "{filename}".')
        sys.exit(1)

    print(f"## {filename} ##")
    print(content.rstrip("\n"))
    print(f"## {filename} ##")

    print("Program ending.")


if __name__ == "__main__":
    main()
