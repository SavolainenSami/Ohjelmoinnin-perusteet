def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    filename = input("Insert filename to read: ")
    print(f'Reading names from "{filename}".')

    try:
        with open(filename, "r", encoding="utf-8") as file:
            names = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')
        print("Program ending.")
        return

    print("Analysing names...")

    if not names:
        print("No valid names found in the file.")
        print("Program ending.")
        return

    name_count = len(names)
    shortest_name = min(len(name) for name in names)
    longest_name = max(len(name) for name in names)
    average_length = sum(len(name) for name in names) / name_count

    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print(f"Name count - {name_count}")
    print(f"Shortest name - {shortest_name} chars")
    print(f"Longest name - {longest_name} chars")
    print(f"Average name - {average_length:.2f} chars")
    print("#### REPORT END ####")
    print("Program ending.")


if __name__ == "__main__":
    main()
