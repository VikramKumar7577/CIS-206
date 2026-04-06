import re

def replace_word(text, old, new):
    result = re.sub(old, new, text)
    print(result)


def main():
    text = "I like apples. Apples are good."
    replace_word(text, "apples", "oranges")


main()