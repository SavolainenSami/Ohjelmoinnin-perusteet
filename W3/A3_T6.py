# main.py
print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")

print("\nOptions:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice = input("Your choice: ")

if choice == "1":
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    sub = input("Your choice: ")

    if sub == "1":
        meters = float(input("Insert meters: "))
        km = round(meters / 1000, 1)
        print(f"{meters} m is {km} km")
    elif sub == "2":
        km = float(input("Insert kilometers: "))
        meters = round(km * 1000, 1)
        print(f"{km} km is {meters} m")
    elif sub == "0":
        print("Exiting...")
    else:
        print("Unknown option.")

elif choice == "2":
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    sub = input("Your choice: ")

    if sub == "1":
        grams = float(input("Insert grams: "))
        pounds = round(grams / 453.59237, 1)
        print(f"{grams} g is {pounds} lb")
    elif sub == "2":
        pounds = float(input("Insert pounds: "))
        grams = round(pounds * 453.59237, 1)
        print(f"{pounds} lb is {grams} g")
    elif sub == "0":
        print("Exiting...")
    else:
        print("Unknown option.")

elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")
