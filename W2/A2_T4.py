print("Program starting.")
print("Estimate how many minutes you spent on programming...\n")

task_1 = int(input("A1_T1: "))
task_2 = int(input("A1_T2: "))
task_3 = int(input("A1_T3: "))
task_4 = int(input("A1_T4: "))
task_5 = int(input("A2_T1: "))
task_6 = int(input("A2_T2: "))
task_7 = int(input("A2_T3: "))

total = task_1 + task_2 + task_3 + task_4 + task_5 + task_6 + task_7
average = float(total / 7)

print(f"\nIn total you spent {total} minutes on programming.")
print(f"Average per task was {round(average,2)} min and same rounded to the nearest integer {round(average)} min.\n")

print("Program ending.")