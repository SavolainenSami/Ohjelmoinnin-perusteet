from dataclasses import dataclass

DELIMITER = ";"


@dataclass
class TIMESTAMP:
    weekday: str = ""
    hour: str = ""
    consumption: float = 0.0
    price: float = 0.0


def readTimestamps(filename: str, timestamps: list[TIMESTAMP]) -> None:
    timestamps.clear()

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


def displayTimestamps(timestamps: list[TIMESTAMP]) -> None:
    print("Electricity usage:")
    for ts in timestamps:
        total = ts.consumption * ts.price
        print(
            f" - {ts.weekday} {ts.hour}, price {ts.price:.2f}, "
            f"consumption {ts.consumption:.2f} kWh, total {total:.2f} €"
        )


def main() -> None:
    print("Program starting.")

    timestamps: list[TIMESTAMP] = []

    filename = input("Insert filename: ")

    readTimestamps(filename, timestamps)
    displayTimestamps(timestamps)

    print("Program ending.")


if __name__ == "__main__":
    main()
