########################################################
# Task A9_T6
# Developer Sami Savolainen
# Date 2025-12-09
########################################################


def showOptions() -> None:
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")


def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except Exception:
        return -1


def saveLines(PLines: list[str]) -> None:
    try:
        filename = input("Insert filename: ")
        with open(filename, "w", encoding="UTF-8") as f:
            f.writelines(PLines)
    except Exception as e:
        print(f"File error: {e}")


def insertLine(PLines: list[str]) -> None:
    text = input("Insert text: ")
    PLines.append(text + "\n")


def onInterrupt(PLines: list[str]) -> None:
    if len(PLines) == 0:
        print("Closing suddenly.")
        print("Program ending.")
        raise SystemExit

    print("Keyboard interrupt and unsaved progress!")
    try:
        choice = input("Save before quit(y/n)?: ").strip().lower()
    except Exception:
        choice = "n"

    if choice == "y":
        try:
            filename = input("Insert filename: ")
            with open(filename, "w", encoding="UTF-8") as f:
                f.writelines(PLines)
        except Exception as e:
            print(f"File error: {e}")

    print("Program ending.")
    raise SystemExit


def main() -> None:
    Lines: list[str] = []
    Choice = -1
    print("Program starting.")

    try:
        while Choice != 0:
            showOptions()
            Choice = askChoice()

            if Choice == 1:
                insertLine(Lines)
            elif Choice == 2:
                saveLines(Lines)
            elif Choice == 0:
                print("Exiting program.")
            else:
                print("Unknown option!")
            print("")
    except KeyboardInterrupt:
        onInterrupt(Lines)

    Lines.clear()
    print("Program ending.")


if __name__ == "__main__":
    main()
