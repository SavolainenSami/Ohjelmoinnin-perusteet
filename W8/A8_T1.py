import time


def print_menu():
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")


def main():
    pause_duration = None

    print("Program starting.")

    while True:
        print_menu()
        choice = input("Your choice: ")

        if choice == "1":
            try:
                pause_duration = float(input("Insert pause duration (s): "))
            except ValueError:
                print("Invalid input!")

        elif choice == "2":
            if pause_duration is None:
                print("Pause is not set.")
                print("Set pause first.")
            else:
                print(f"Pausing for {pause_duration} seconds.")
                time.sleep(pause_duration)
                print("Unpaused.")

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Unknown option!")

        print()

    print("Program ending.")


if __name__ == "__main__":
    main()
