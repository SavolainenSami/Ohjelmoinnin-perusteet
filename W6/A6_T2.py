def writeFile(PFilename, PContent) -> None:
    Filehandle = open(PFilename, "w")
    Filehandle.write(PContent)
    Filehandle.close()
    return None


def main() -> None:
    print("Program starting")
    FirstName = input("Insert first name: ")
    LastName = input("Insert last name: ")
    Filename = input("Insert filename: ")
    Content = "{}\n{}".format(FirstName, LastName)
    writeFile(Filename, Content)
    print("Program ending")
    return None


if __name__ == "__main__":
    main()
