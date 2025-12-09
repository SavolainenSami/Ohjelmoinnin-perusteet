########################################################
# Task A9_T5
# Developer Sami Savolainen
# Date 2025-12-09
########################################################


def askIntByte(PPrompt: str) -> int:
    Feed = input(PPrompt)

    try:
        value_float = float(Feed)

        if not value_float.is_integer():
            raise Exception("Not an integer")

        value = int(value_float)

        if not (0 <= value <= 255):
            raise Exception("Out of range")

        return value

    except:
        raise


def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(PRed, PGreen, PBlue)


def main():
    print("Program starting.")

    try:
        r = askIntByte("Insert red: ")
        g = askIntByte("Insert green: ")
        b = askIntByte("Insert blue: ")

        hex_color = createHex(r, g, b)

        print("RGB Details:")
        print(f"- Red {r}")
        print(f"- Green {g}")
        print(f"- Blue {b}")
        print(f"- Hex {hex_color}")

        print(f"{r:08b}")
        print(f"{g:08b}")
        print(f"{b:08b}")

    except:
        print("Couldn't perform the designed task")

    print("Program ending.")


if __name__ == "__main__":
    main()
