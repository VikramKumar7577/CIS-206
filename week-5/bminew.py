def get_weight():
    """Ask for weight in pounds and return it. Type Q to quit."""
    while True:
        text = input("Weight (pounds): ").strip()

        # Activity 1: user can quit
        if text.upper() == "Q":
            return None

        # Activity 1: if bad input, do not end program
        try:
            weight = float(text)
        except ValueError:
            print("Error: please enter a number (or Q to quit).")
            continue

        if weight <= 0:
            print("Error: weight must be greater than 0.")
            continue

        return weight


def get_height_inches():
    """Ask for height in feet and inches and return total inches. Type Q to quit."""
    while True:
        feet_text = input("Height feet: ").strip()

        # Activity 1: user can quit
        if feet_text.upper() == "Q":
            return None

        try:
            feet = int(feet_text)
        except ValueError:
            print("Error: feet must be a whole number (or Q to quit).")
            continue

        if feet <= 0:
            print("Error: feet must be greater than 0.")
            continue

        inches_text = input("Height inches: ").strip()

        # Activity 1: user can quit
        if inches_text.upper() == "Q":
            return None

        try:
            inches = int(inches_text)
        except ValueError:
            print("Error: inches must be a whole number (or Q to quit).")
            continue

        if inches < 0 or inches > 11:
            print("Error: inches must be between 0 and 11.")
            continue

        total_inches = (feet * 12) + inches
        return total_inches


def calculate_bmi(weight_pounds, height_inches):
    """Calculate BMI using pounds and inches."""
    return (weight_pounds * 703) / (height_inches ** 2)


def bmi_category(bmi):
    """Return BMI category using CDC adult ranges."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def print_bmi_table():
    """Print BMI table (heights 58-76 step 2, weights 100-250 step 10)."""
    print("\nBMI Table (weight x height)")
    print("Heights are inches. Weights are pounds.\n")

    heights = list(range(58, 77, 2))

    # header row
    print("wt\\ht", end="")
    for h in heights:
        print(f"{h:>6}", end="")
    print()

    # table rows
    for weight in range(100, 251, 10):
        print(f"{weight:>5}", end="")
        for h in heights:
            bmi = calculate_bmi(weight, h)
            print(f"{bmi:>6.1f}", end="")
        print()


def main():
    """Run the BMI program (loops until the user quits)."""
    print("BMI Calculator")
    print("Type Q at any prompt to quit.\n")

    # Activity 2: loop the program for multiple BMI checks
    while True:
        weight = get_weight()
        if weight is None:
            break

        height_inches = get_height_inches()
        if height_inches is None:
            break

        bmi = calculate_bmi(weight, height_inches)
        category = bmi_category(bmi)

        print("\nYour BMI is:", round(bmi, 1))
        print("Category:", category)

        print("\nBMI Legend:")
        print("Underweight: < 18.5")
        print("Healthy:     18.5 - 24.9")
        print("Overweight:  25.0 - 29.9")
        print("Obesity:     30.0+")

        again = input("\nDo another BMI? (Y/N): ").strip().upper()
        if again != "Y":
            break

    # Activity 4: show the BMI table (reuses calculate_bmi)
    print_bmi_table()


main()