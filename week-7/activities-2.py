def encode_string(text):

    #Encode a string using run length encoding


    if not text.isalpha():
        return None

    encoded = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded += text[i - 1]
            if count > 1:
                encoded += str(count)
            count = 1

    encoded += text[-1]
    if count > 1:
        encoded += str(count)

    return encoded


def decode_string(text):

    #Decode a run length encoded string


    decoded = ""
    i = 0

    while i < len(text):
        char = text[i]
        i += 1

        number = ""

        while i < len(text) and text[i].isdigit():
            number += text[i]
            i += 1

        if number == "":
            decoded += char
        else:
            decoded += char * int(number)

    return decoded


def main():

    user_input = input("Enter a string: ")

    if any(char.isdigit() for char in user_input):
        result = decode_string(user_input)
        print("Decoded string:", result)
    else:
        if not user_input.isalpha():
            print("Error: Only alphabetic characters allowed.")
            return
        result = encode_string(user_input)
        print("Encoded string:", result)


main()