import re

def check_string(text):
    pattern = r'\b\w*z\w*\b'

    match = re.search(pattern, text)

    if match:
        print("Word with z:", match.group())
    else:
        print("No match")


def main():
    check_string("The quick brown fox jumps over the lazy dog.")
    check_string("Python Exercises.")


main()