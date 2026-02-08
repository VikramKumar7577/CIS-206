def get_float(prompt):
    ## Ask for a decimal number. Returns None if it is not a number.
    ## 2 Exception handling (try/except)
    try:
        return float(input(prompt))
    except ValueError:
        return None


def get_int(prompt):
    ## Ask for a whole number. Returns None if it is not a whole number.
    ## 2 Exception handling (try/except)
    try:
        return int(input(prompt))
    except ValueError:
        return None


def main():
    print("Tip Splitter\n")

    bill = get_float("Bill amount ($): ")

    ## 1 Validation check (data type)
    if bill is None:
        print("Error: bill must be a number.")
        return

    ## 1 Validation check (range/constraint)
    if bill <= 0:
        print("Error: bill must be greater than 0.")
        return

    tip_percent = get_float("Tip percent (example 15 for 15%): ")

    ## 1 Validation check (data type)
    if tip_percent is None:
        print("Error: tip percent must be a number.")
        return

    ## 1 Validation check (range/constraint)
    if tip_percent < 0 or tip_percent > 100:
        print("Error: tip percent must be between 0 and 100.")
        return

    people = get_int("Number of people: ")

    ## 1 Validation check (data type)
    if people is None:
        print("Error: number of people must be a whole number.")
        return

    ## 1 Validation check (range/constraint)
    if people < 1:
        print("Error: number of people must be at least 1.")
        return

    tip_amount = bill * (tip_percent / 100)
    total = bill + tip_amount
    per_person = total / people

    print("\nResults")
    print("Bill:      $", round(bill, 2))
    print("Tip:       $", round(tip_amount, 2))
    print("Total:     $", round(total, 2))
    print("Per person:$", round(per_person, 2))

    ## 3 Nested if statement
    if people >= 6:
        if tip_percent < 18:
            print("\nLarge group note: 18% tip is common.")
        else:
            print("\nLarge group note: tip looks good.")


main()