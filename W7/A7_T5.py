from dataclasses import dataclass

DELIMITER = ";"


@dataclass
class TIMESTAMP:
    weekday: str = ""
    hour: str = ""
    consumption: float = 0.0
    price: float = 0.0


@dataclass
class DAY_USAGE:
    weekday: str
    consumption: float = 0.0
    cost: float = 0.0


WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturnday",
    "Sunday",
]


def readTimestamps(filename: str, timestamps: list[TIMESTAMP]) -> None:
    timestamps.clear()
    print(f'Reading file "{filename}".')

    try:
        with open(filename, "r", encoding="utf-8") as file:
            first = True
            for line in file:
                row = line.rstrip("\n")

                if first:
                    first = False
                    continue

                if row == "":
                    continue

                cols = row.split(DELIMITER)

                ts = TIMESTAMP(
                    weekday=cols[0],
                    hour=cols[1],
                    consumption=float(cols[2]),
                    price=float(cols[3]),
                )
                timestamps.append(ts)

    except FileNotFoundError:
        print(f'Error: file "{filename}" cannot be opened.')


def analyseTimestamps(timestamps: list[TIMESTAMP]) -> list[DAY_USAGE]:
    print("Analysing timestamps.")

    summary = {day: DAY_USAGE(day) for day in WEEKDAYS}

    for ts in timestamps:
        if ts.weekday in summary:
            summary[ts.weekday].consumption += ts.consumption
            summary[ts.weekday].cost += ts.consumption * ts.price

    return [summary[day] for day in WEEKDAYS]


def displayResults(results: list[DAY_USAGE]) -> None:
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for day in results:
        print(
            f" - {day.weekday} usage {day.consumption:.2f} kWh, "
            f"cost {day.cost:.2f} €"
        )
    print("### Electricity consumption summary ###")


def main() -> None:
    print("Program starting.")

    timestamps: list[TIMESTAMP] = []

    filename = input("Insert filename: ")

    readTimestamps(filename, timestamps)
    results = analyseTimestamps(timestamps)
    displayResults(results)

    print("Program ending.")


if __name__ == "__main__":
    main()
