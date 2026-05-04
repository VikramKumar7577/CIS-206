import json
import xml.etree.ElementTree as ET


def read_json_file():
    with open("books.json", "r") as file:
        data = json.load(file)

    return data["books"]


def read_xml_file():
    tree = ET.parse("books.xml")
    root = tree.getroot()

    books = []

    for book in root.findall("book"):
        books.append({
            "title": book.find("title").text,
            "author": book.find("author").text,
            "year": book.find("year").text,
            "available": book.find("available").text
        })

    return books


def display_books(books):
    print("Books in file:")

    for book in books:
        print(book["title"], "-", book["author"], "-", book["year"])


def search_books(books):
    while True:
        title = input("\nEnter book title or quit to stop: ")

        if title.lower() == "quit":
            break

        found = False

        for book in books:
            if book["title"].lower() == title.lower():
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Year:", book["year"])
                found = True

        if not found:
            print(title, "title not found")


def main():
    print("JSON Test")
    json_books = read_json_file()
    display_books(json_books)
    search_books(json_books)

    print("\nXML Test")
    xml_books = read_xml_file()
    display_books(xml_books)
    search_books(xml_books)


main()