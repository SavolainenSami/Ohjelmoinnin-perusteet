print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))
print()

errors = []

if start >= stop:
    errors.append("Starting point value must be less than the stopping point value.")
if not (start <= inspect <= stop):
    errors.append("Inspection value must be within the range of start and stop.")

if errors:
    for e in errors:
        print(e)
    print("\nProgram ending.")
else:
    print("First loop - inspection with break:")
    line = []
    for i in range(start, stop):
        if i == inspect:
            break
        line.append(str(i))
    print(" ".join(line))

    print("Second loop - inspection with continue:")
    line = []
    for i in range(start, stop):
        if i == inspect:
            continue
        line.append(str(i))
    print(" ".join(line))

    print("\nProgram ending.")
