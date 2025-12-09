########################################################
# Task A9_T7
# Developer Sami Savolainen
# Date 2025-12-09
########################################################

import sys
import os


def showHelp() -> None:
    print("[USAGE] python A9_T7.py src_file dst_file")


def copyFile(PSrcFile: str, PDstFile: str) -> None:
    print(f'Source file "{PSrcFile}"')
    print(f'Destination file "{PDstFile}"')
    print(f'Copying file "{PSrcFile}" to "{PDstFile}".')

    proceed = True

    if os.path.exists(PDstFile):
        print(f'Destination file "{PDstFile}" already exists.')
        ans = input("Do you want to overwrite it? (y/n): ").lower()
        if ans != "y":
            proceed = False

    if proceed:
        try:
            with open(PSrcFile, "r") as src:
                data = src.read()

            with open(PDstFile, "w") as dst:
                dst.write(data)

        except:
            print(f'Couldn\'t copy "{PSrcFile}" to "{PDstFile}".')
            print("Exiting program.")
            sys.exit(-1)


def main() -> None:
    print("Program starting.")

    if len(sys.argv) != 3:
        print("Invalid amount of arguments.")
        showHelp()
        print("Program ending.")
        return

    src = sys.argv[1]
    dst = sys.argv[2]

    copyFile(src, dst)

    print("Program ending.")


if __name__ == "__main__":
    main()
