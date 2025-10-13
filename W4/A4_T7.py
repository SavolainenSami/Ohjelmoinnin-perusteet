print("Program starting.\n")
print("Check multiplicative persistence.")
user_input = input("Insert an integer: ")

num = int(user_input)
steps = 0

while num >= 10:
    digits = [int(d) for d in str(num)]
    expression = " * ".join(str(d) for d in digits)
    
    result = 1
    for d in digits:
        result *= d

    print(f"{expression} = {result}")
    num = result
    steps += 1

print("No more steps.\n")
print(f"This program took {steps} step(s)\n")
print("Program ending.")
