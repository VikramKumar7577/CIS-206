import re

def replace_chars(text):
    pattern = r'[ ,.]+'
    result = re.sub(pattern, ':', text)

    print(result)


def main():
    text = "Python Exercises, PHP exercises."
    replace_chars(text)


main()