print("Program starting.")

print("String comparison.")

word1 = input("Insert first word: ")

char = input("Insert a character: ")

if (char in word1):
  print(f"Word \"{word1}\" contains character \"{char}\".")
else:
  print(f"Word \"{word1}\" doesn't contain character \"{char}\".")

word2 = input("Insert second word: ")
if (word1 < word2):
  print(f"The first \"{word1}\" is before the second word \"{word2}\" in alphabetically.")
elif (word1 > word2):
  print(f"The second \"{word2}\" is before the first word \"{word1}\" in alphabetically.")
else:
  print(f"Both inserted words are the same alphabetically, \"{word1}\"")

print("Program ending.")