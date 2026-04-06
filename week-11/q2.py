import re

def check_string(text):
    pattern = r'^ab*$'

    if re.fullmatch(pattern, text):
        print(text, "-> Match")
    else:
        print(text, "-> No match")


def main():
    check_string("ab")
    check_string("abc")
    check_string("a")
    check_string("ab")
    check_string("abb")


main()