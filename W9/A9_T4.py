########################################################
# Task A9_T4
# Developer Sami Savolainen
# Date 2025-12-09
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000


def collectCelsius(feed):
    try:
        c = float(feed)
    except ValueError:
        raise ValueError(f"could not convert string to float: '{feed}'")

    if c < TEMP_MIN or c > TEMP_MAX:
        raise Exception(f"{c} temperature out of range.")

    return c


def main():
    print("Program starting.")

    user_input = input("Insert Celsius: ")

    try:
        value = collectCelsius(user_input)
        print(f"You inserted {value} °C")
    except Exception as e:
        print(e)

    print("Program ending.")


if __name__ == "__main__":
    main()
