print("Program starting.\n")

start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))

print("\nStarting while-loop:")

current = start

while current <= stop:
    print(current, end=" ")
    current += 1

print("\n")

print("Program ending.")