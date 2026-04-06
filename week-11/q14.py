import re

def find_words(text):
    pattern = r'\b[aAeE]\w*'
    matches = re.findall(pattern, text)

    print(matches)


def main():
    text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
    find_words(text)


main()