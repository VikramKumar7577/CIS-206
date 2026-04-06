import re

def search_words(text, words):
    for word in words:
        match = re.search(word, text)

        if match:
            print(word, "-> Found")
        else:
            print(word, "-> Not found")


def main():
    text = "The quick brown fox jumps over the lazy dog."
    words = ["fox", "dog", "horse"]

    search_words(text, words)


main()