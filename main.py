def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        # reading file into file_contents
        file_contents = f.read()

        # processing of text before print report
        words = count_words(file_contents)
        chars_dict = count_chars(file_contents)
        chars_list = list(chars_dict)
        new_list = []
        for char in chars_list:
            if char.isalpha():
                new_list.append(char)
        new_list.sort()

        # printing the report

        print(f"--- Begin report of {path} ---")
        print(f"{words} words found in the document")
        for letter in new_list:
            print(f"The '{letter}' character was found {chars_dict[letter]} times")
        print(f"--- End report of {path} ---")


def count_words(file_contents):
    count = 0
    for word in file_contents.split():
        count = count + 1
    return count


def count_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


if __name__ == "__main__":
    main()
