import re

def check_string(text):
    pattern = r'^[a-zA-Z0-9]+$'

    if re.fullmatch(pattern, text):
        print(text, "-> Valid")
    else:
        print(text, "-> Not valid")


def main():
    check_string("ABCDEFabcdef123450")
    check_string("*&%@#!}{")


main()