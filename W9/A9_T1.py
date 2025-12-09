########################################################
# Task A9_T1
# Developer Sami Savolainen
# Date 2025-12-09
########################################################


def main():
    print("Program starting.\n")

    total = 0.0

    while True:
        user_input = input("Insert a floating-point value (0 to stop): ")

        if user_input == "0":
            break

        try:
            value = float(user_input)
            total += value
        except ValueError:
            print("Error! '{}' couldn't be converted to float.".format(user_input))
            continue

    print("\nFinal sum is {:.2f}".format(total))
    print("Program ending.")


if __name__ == "__main__":
    main()
