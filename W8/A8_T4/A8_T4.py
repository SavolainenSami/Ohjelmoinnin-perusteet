# main.py
from timestamp_lib import (
    readTimestamps,
    calculateYears,
    calculateMonths,
    calculateWeekdays,
)


def print_menu() -> None:
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ").strip()

    timestamps = []
    try:
        readTimestamps(filename, timestamps)
    except FileNotFoundError:
        print(f"Error: file '{filename}' was not found.")
        print("Program ending.")
        return
    except ValueError as e:
        print(f"Error while reading timestamps: {e}")
        print("Program ending.")
        return

    while True:
        print_menu()
        choice = input("Your choice: ").strip()

        if choice == "0":
            print("Exiting program.")
            print("Program ending.")
            break

        elif choice == "1":
            year_str = input("Insert year: ").strip()
            try:
                year = int(year_str)
            except ValueError:
                print("Invalid year. Please insert a number like 2000.")
                continue

            count = calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {count}")

        elif choice == "2":
            month_input = input("Insert month: ").strip()
            try:
                count = calculateMonths(month_input, timestamps)
                print(f"Amount of timestamps during month '{month_input}' is {count}")
            except ValueError:
                print("Invalid month. Please insert a month name like April.")

        elif choice == "3":
            weekday_input = input("Insert weekday: ").strip()
            try:
                count = calculateWeekdays(weekday_input, timestamps)
                print(
                    f"Amount of timestamps during weekday '{weekday_input}' is {count}"
                )
            except ValueError:
                print("Invalid weekday. Please insert a weekday name like Monday.")

        else:
            print("Invalid choice. Please choose 0–3.")


if __name__ == "__main__":
    main()
