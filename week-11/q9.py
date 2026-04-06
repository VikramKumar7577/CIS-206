import re

def search_word(text, word):
    match = re.search(word, text)

    if match:
        print(word, "found at position", match.start())
    else:
        print(word, "not found")


def main():
    text = "The quick brown fox jumps over the lazy dog."
    search_word(text, "fox")


main()