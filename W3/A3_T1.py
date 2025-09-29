print("Program starting.")
print("Insert two integers.")

int1 = int(input("Insert first integer: "))
int2 = int(input("Insert second integer: "))

print("Comaring the integers.")
if (int1 > int2):
    print("First integer is greater.")
elif (int1 < int2):
    print("Second integer is greater.")
else:
    print("The integers are same.")
print("")

sum = int1 + int2
print(f"{int1} + {int2} = {sum}")
print("")

remainder = sum % 2

if (remainder == 0):
    print("Sum is eaven.")
else:
    print("Sum is odd.")
    
print("Program ending.")
