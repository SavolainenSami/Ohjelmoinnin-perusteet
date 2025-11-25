def main():
    print("Program starting.")
    print("This program can copy a file.")

    source_filename = input("Insert source filename: ")
    destination_filename = input("Insert destination filename: ")

    print(f"Reading file '{source_filename}' content.")
    with open(source_filename, "r", encoding="utf-8") as source_file:
        content = source_file.read()

    print("File content ready in memory.")

    print(f"Writing content into file '{destination_filename}'.")
    with open(destination_filename, "w", encoding="utf-8") as dest_file:
        dest_file.write(content)

    print("Copying operation complete.")
    print("Program ending.")


if __name__ == "__main__":
    main()
