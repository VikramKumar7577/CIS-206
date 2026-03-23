import csv

def read_file(filename):
    customers = []
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers.append(row)
    return customers


def display_by_company(customers):
    sorted_list = sorted(customers, key=lambda x: x['CompanyName'])
    for c in sorted_list:
        print(f"{c['CompanyName']} | {c['ContactName']} | {c['Phone']}")


def display_by_contact(customers):
    sorted_list = sorted(customers, key=lambda x: x['ContactName'])
    for c in sorted_list:
        print(f"{c['ContactName']} | {c['CompanyName']} | {c['Phone']}")


def search_company(customers, name):
    found = False
    for c in customers:
        if name.lower() in c['CompanyName'].lower():
            print("\nCompany:", c['CompanyName'])
            print("Contact:", c['ContactName'])
            print("Phone:", c['Phone'])
            found = True
    if not found:
        print("No matches found.")


def search_contact(customers, name):
    found = False
    for c in customers:
        if name.lower() in c['ContactName'].lower():
            print("\nCompany:", c['CompanyName'])
            print("Contact:", c['ContactName'])
            print("Phone:", c['Phone'])
            found = True
    if not found:
        print("No matches found.")


def main():
    customers = read_file("customers.txt")

    while True:
        print("\n1. Show by company")
        print("2. Show by contact")
        print("3. Search company")
        print("4. Search contact")
        print("5. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            display_by_company(customers)
        elif choice == "2":
            display_by_contact(customers)
        elif choice == "3":
            name = input("Enter company name: ").strip()
            search_company(customers, name)
        elif choice == "4":
            name = input("Enter contact name: ").strip()
            search_contact(customers, name)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")


main()