########################################################
# Task A9_T2
# Developer Sami Savolainen
# Date 2025-12-09
########################################################

import sys


def main():
    print("Program starting.")

    user_input = input("Insert exit code(0-255): ")

    try:
        code = int(user_input)
    except ValueError:
        print("Invalid input! Must be an integer between 0–255.")
        sys.exit(1)

    if code < 0 or code > 255:
        print("Invalid range! Exit code must be 0–255.")
        sys.exit(1)

    if code == 0:
        print("Clean exit")
    else:
        print("Error code")

    sys.exit(code)


if __name__ == "__main__":
    main()
