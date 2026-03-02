def encode_string(text):

    #Encode a string using RLE with escape support


    encoded = "##00"
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

    #Decode a string that starts with ##00.


    if not text.startswith("##00"):
        return None

    text = text[4:]
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

    #Main program with validation.


    user_input = input("Enter a string: ")

    if user_input.startswith("##00"):
        result = decode_string(user_input)
        print("Decoded string:", result)
    else:
        result = encode_string(user_input)
        print("Encoded string:", result)


main()