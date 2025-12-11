def readValues(PFilename: str, PValues: list[int]) -> None:
    with open(PFilename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                PValues.append(int(line))


def displayValues(PValues: list[int]) -> str:
    return ", ".join(str(v) for v in PValues)


def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if PAsc:
                if PValues[j] > PValues[j + 1]:
                    PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
            else:
                if PValues[j] < PValues[j + 1]:
                    PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
