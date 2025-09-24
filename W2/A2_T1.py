print("Program starting.")

Name = input("What is your name: ")

First_Number = input("Enter a floating point number: ")
First_Number = float(First_Number)

Secend_Number = input("Enter second floating point number: ")
Secend_Number = float(Secend_Number)

print(f"{Name} you gave numbers {First_Number} and {Secend_Number}")

Multi = First_Number * Secend_Number
print(f"Multiplying first and second  will result in product {round(Multi, 2)}")

print("Program ending.")