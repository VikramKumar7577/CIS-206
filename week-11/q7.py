def remove_zeros(ip):
    parts = ip.split(".")
    new_parts = []

    for part in parts:
        new_parts.append(str(int(part)))

    result = ".".join(new_parts)
    print(result)


def main():
    remove_zeros("216.08.094.196")


main()