def askName() -> str:
    name = input("Insert name: ")
    return name


def greedUser(Pname) -> None:
    print(f"Hello {Pname}")
    return None


def main() -> None:
    print("Program starting.")
    name = askName()
    greedUser(name)
    print("Program ending.")
    return None


main()
