print("Program starting.")
n = int(input("Insert a positive integer: "))
steps = 0
sequence = [str(n)]

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    sequence.append(str(n))
    steps += 1

print(" -> ".join(sequence))
print(f"Sequence had {steps} total steps.\n")
print("Program ending.")
