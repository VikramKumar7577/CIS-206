def load_names(filename):
    #Load names from the file and return them as a list
    file = open(filename, "r")
    names = []

    for line in file:
        names.append(line.strip())

    file.close()
    return names


def main():

    names = load_names("names.txt")

    while True:

        user_name = input("Enter a name to search (or Q to quit): ")

        if user_name.upper() == "Q":
            print("Program ended.")
            break

        if user_name in names:
            print(user_name + " was found in the file.")
        else:
            print(user_name + " was NOT found. Writing to nofound.txt")

            outfile = open("nofound.txt", "a")
            outfile.write(user_name + "\n")
            outfile.close()


main()