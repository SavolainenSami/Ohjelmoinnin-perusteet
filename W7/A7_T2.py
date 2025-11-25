def main():
    print("Program starting.")

    user_input = input("Insert comma separated integers: ")

    parts = user_input.split(",")

    valid_integers: list[int] = []

    for p in parts:
        value = p.strip()
        try:
            number = int(value)
            valid_integers.append(number)
        except ValueError:
            print(f"Invalid value '{value}' detected.")

    if len(valid_integers) == 0:
        print("No values to analyse.")
        print("Program ending.")
        return

    total = sum(valid_integers)
    count = len(valid_integers)
    even_or_odd = "even" if total % 2 == 0 else "odd"

    print(f"There are {count} integers in the list.")
    print(f"Sum of the integers is {total} and it's {even_or_odd}")
    print("Program ending.")


if __name__ == "__main__":
    main()
