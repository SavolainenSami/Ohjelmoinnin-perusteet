def read_values(filename):
    values = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    values.append(float(line))
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except ValueError:
        print(f"File {filename} contains non-numeric values.")
    return values


def amount_of_values(values):
    return len(values)


def sum_of_values(values):
    return round(sum(values), 1)


def average_of_values(values):
    if values:
        return round(sum(values) / len(values), 1)
    else:
        return 0.0


def main():
    values = []
    print("Program starting.")
    while True:
        print("\nOptions:")
        print("1 - Read values")
        print("2 - Amount of values")
        print("3 - Calculate sum of values")
        print("4 - Calculate average of values")
        print("0 - Exit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            filename = input("Insert filename: ").strip()
            values = read_values(filename)
        elif choice == "2":
            print(f"Amount of values {amount_of_values(values)}")
        elif choice == "3":
            print(f"Sum of values {sum_of_values(values)}")
        elif choice == "4":
            print(f"Average of values {average_of_values(values)}")
        elif choice == "0":
            print("Exiting program.\n\nProgram ending.")
            break
        else:
            print("Invalid choice. Please select 0-4.")


if __name__ == "__main__":
    main()
