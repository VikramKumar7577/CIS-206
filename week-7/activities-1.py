def encode_string(text):

   # Encode a string using basic run length encoding
   # Only alphabetic characters are allowed
   # Returns the encoded string

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

    # add last character
    encoded += text[-1]
    if count > 1:
        encoded += str(count)

    return encoded


def main():

    #Main function to run the encoder program.

    user_input = input("Enter alphabetic characters only: ")

    if not user_input.isalpha():
        print("Error: Only alphabetic characters are allowed.")
        return

    result = encode_string(user_input)
    print("Encoded string:", result)


main()