WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturnday",
    "Sunday",
)


def readFile(PFilename: str, PRows: list[str]) -> None:
    print(f'Reading file "{PFilename}".')

    PRows.clear()

    try:
        with open(PFilename, "r", encoding="utf-8") as f:
            first = True
            for line in f:
                if first:
                    first = False
                    continue

                line = line.rstrip("\n")

                if line == "":
                    continue

                PRows.append(line)

    except FileNotFoundError:
        print("Error: File not found.")
    return None


def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")

    PResults.clear()

    WeekdayTimestampAmount = [0, 0, 0, 0, 0, 0, 0]

    for row in PRows:
        for i, weekday in enumerate(WEEKDAYS):
            if row.startswith(weekday):
                WeekdayTimestampAmount[i] += 1

    for i, weekday in enumerate(WEEKDAYS):
        PResults.append(f" - {weekday} {WeekdayTimestampAmount[i]} stamps")

    return None


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for line in PResults:
        print(line)
    print("### Timestamp analysis ###")
    return None


def main() -> None:
    print("Program starting.")

    rows: list[str] = []
    results: list[str] = []

    filename = input("Insert filename: ")

    readFile(filename, rows)
    analyseTimestamps(rows, results)
    displayResults(results)

    rows.clear()
    results.clear()

    print("Program ending.")
    return None


main()
