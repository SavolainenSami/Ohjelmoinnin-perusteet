print("Program starting.\n")

hex_color = input("Insert a hex color: ").strip()

if len(hex_color) != 7 or not hex_color.startswith("#"):
    print("Invalid hex color format. It should start with '#' and be 7 characters long.")
else:
    red = hex_color[1:3]
    green = hex_color[3:5]
    blue = hex_color[5:7]

    print("\nColors")
    print(f"- Red {red}")
    print(f"- Green {green}")
    print(f"- Blue {blue}")

print("\nProgram ending.")
