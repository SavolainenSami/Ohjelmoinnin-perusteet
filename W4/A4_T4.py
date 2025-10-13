print("Program starting.\n")

words = []
total_characters = 0

while True:
    word = input("Insert word (empty stops): ")
    if word == "":
        break
    words.append(word)
    total_characters += len(word)

print("\nYou inserted:")
print(f"- {len(words)} words")
print(f"- {total_characters} characters")

print("\nProgram ending.")