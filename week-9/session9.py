def load_customers(filename):
    customers = []

    file = open(filename, "r")

    for line in file:
        parts = line.strip().split(",")
        customers.append(parts)

    file.close()

    return customers


def display_by_company(customers):

    sorted_list = sorted(customers, key=lambda c: c[1])

    for c in sorted_list:
        print(c[1], "-", c[2], "-", c[3], "-", c[4])


def display_by_contact(customers):

    sorted_list = sorted(customers, key=lambda c: c[2])

    for c in sorted_list:
        print(c[1], "-", c[2], "-", c[3], "-", c[4])


def search_company(customers):

    name = input("Enter company name: ")

    found = False

    for c in customers:
        if name.lower() in c[1].lower():
            print(c[1], "-", c[2], "-", c[3], "-", c[4])
            found = True

    if not found:
        print("No company found.")


def search_contact(customers):

    name = input("Enter contact name: ")

    found = False

    for c in customers:
        if name.lower() in c[2].lower():
            print(c[1], "-", c[2], "-", c[3], "-", c[4])
            found = True

    if not found:
        print("No contact found.")


def show_menu():

    print()
    print("1. Display customers sorted by company name")
    print("2. Display customers sorted by contact name")
    print("3. Search customers by company name")
    print("4. Search customers by contact name")
    print("5. Exit")


def main():

    customers = load_customers("customers.txt")

    while True:

        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            display_by_company(customers)

        elif choice == "2":
            display_by_contact(customers)

        elif choice == "3":
            search_company(customers)

        elif choice == "4":
            search_contact(customers)

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


main()