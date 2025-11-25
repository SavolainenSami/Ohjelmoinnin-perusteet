def readFile(Filename):
    Filehandler = open(Filename, "r")
    Content = ""
    Row = Filehandler.readline()
    while Row != "":
        Content += Row
        Row = Filehandler.readline()
    Filehandler.close()
    return Content


def main() -> None:
    print("Program starting.")
    print("This program can read a file.")
    Filename = input("Insert filename: ")
    FileContent = readFile(Filename)
    print("#### START {} ####".format(Filename))
    print(FileContent)
    print("#### END {} ####".format(Filename))
    return None


if __name__ == "__main__":
    main()
