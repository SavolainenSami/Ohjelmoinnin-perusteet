########################################################
# Task A10_T1
# Developer Sami Savolainen
# Date 2025-12-11
########################################################


def main():
    print("Program starting.")
    filename = input("Insert filename: ")

    try:
        with open(filename, "r") as file:
            values = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        print("Program ending.")
        return

    print("# --- Vertically --- #")
    for v in values:
        print(v)
    print("# --- Vertically --- #")

    print("# --- Horizontally --- #")
    print(", ".join(values))
    print("# --- Horizontally --- #")

    print("Program ending.")


if __name__ == "__main__":
    main()
