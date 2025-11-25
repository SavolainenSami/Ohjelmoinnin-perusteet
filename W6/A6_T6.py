LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shiftCharacter(char, alphabet):
    if char not in alphabet:
        return char
    index = alphabet.index(char)
    shifted_index = (index + 13) % 26
    return alphabet[shifted_index]


def rot13(text):
    result = ""
    for ch in text:
        if ch in LOWER_ALPHABETS:
            result += shiftCharacter(ch, LOWER_ALPHABETS)
        elif ch in UPPER_ALPHABETS:
            result += shiftCharacter(ch, UPPER_ALPHABETS)
        else:
            result += ch
    return result


def writeFile(filename, content):
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(content)


def main():
    print("Program starting.\n")
    print("Collecting plain text rows for ciphering.")
    lines = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        lines.append(row)

    print("\n#### Ciphered text ####")
    ciphered_lines = [rot13(line) for line in lines]
    for line in ciphered_lines:
        print(line)

    print("\n#### Ciphered text ####")
    filename = input("Insert filename to save: ")
    if filename.strip() == "":
        print("File name not defined.")
        print("Aborting save operation.")
        print("Program ending.")
        return

    content = "\n".join(ciphered_lines) + "\n"
    writeFile(filename, content)
    print("Ciphered text saved!")
    print("Program ending.")


if __name__ == "__main__":
    main()
