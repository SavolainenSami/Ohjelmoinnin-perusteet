########################################################
# Task A10_T5
# Developer Sami Savolainen
# Date 2025-12-11
########################################################


def recursiveFactorial(PNum: int) -> int:
    if PNum <= 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)


def main() -> None:
    print("Program starting.")
    num = int(input("Insert factorial: "))

    print(f"Factorial {num}!")

    if num <= 1:
        sequence = "1"
    else:
        sequence = "*".join(str(i) for i in range(1, num + 1))

    result = recursiveFactorial(num)

    print(f"{sequence} = {result}")

    print("Program ending.")


if __name__ == "__main__":
    main()
