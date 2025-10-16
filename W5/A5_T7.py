DELIMITER = ","


def collectWords():
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    return DELIMITER.join(words)


def analyseWords(words_string):
    words = words_string.split(DELIMITER) if words_string else []
    word_count = len(words)
    char_count = sum(len(word) for word in words)
    avg_length = char_count / word_count if word_count > 0 else 0
    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print("- {:.2f} Average word length".format(avg_length))


def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")


main()
