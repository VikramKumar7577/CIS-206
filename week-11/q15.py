import re

def clean_spaces(text):
    result = re.sub(r'\s+', ' ', text)
    print(result)


def main():
    text = "Python      Exercises"
    clean_spaces(text)


main()