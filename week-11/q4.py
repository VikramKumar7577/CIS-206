import re

def check_string(text):
    pattern = r'^[a-z]+_[a-z]+$'

    if re.fullmatch(pattern, text):
        print(text, "-> Match")
    else:
        print(text, "-> No match")


def main():
    check_string("aab_cbbbc")
    check_string("aab_Abbbc")
    check_string("Aaab_abbbc")


main()