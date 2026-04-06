import re

def extract_date(url):
    match = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', url)

    if match:
        print("Year:", match.group(1))
        print("Month:", match.group(2))
        print("Date:", match.group(3))


def main():
    url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
    extract_date(url)


main()