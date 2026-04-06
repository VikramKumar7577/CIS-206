import re

def check_string(text):
    pattern = r'^\w+'

    match = re.match(pattern, text)

    if match:
        print("Word at start:", match.group())
    else:
        print("No match")


def main():
    check_string("The quick brown fox jumps over the lazy dog.")
    check_string(" The quick brown fox jumps over the lazy dog.")


main()