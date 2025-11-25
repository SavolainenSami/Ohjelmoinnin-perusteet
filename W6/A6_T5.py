SEPARATOR = ";"


def readValues(filename: str) -> str:
    values = ""
    with open(filename, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            number = line.strip()
            if i < len(lines) - 1:
                values += number + SEPARATOR
            else:
                values += number
    return values


def analyseValues(values: str) -> str:
    numbers = [int(x) for x in values.split(SEPARATOR) if x.strip().isdigit()]

    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count if count > 0 else 0

    result = (
        "Count;Sum;Greatest;Average\n" f"{count};{total};{greatest};{average:.2f}\n"
    )
    return result


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    values = readValues(filename)
    result = analyseValues(values)
    print(result)
    print("#### Number analysis - END ####")
    print("Program ending.")


if __name__ == "__main__":
    main()
