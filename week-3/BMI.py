def get_weight():
    """Ask for weight in pounds and return it."""
    return float(input("Weight (pounds): "))


def get_height_inches():
    """Ask for height in feet and inches and return total inches."""
    feet = int(input("Height feet: "))
    inches = int(input("Height inches: "))

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


def main():
    """Run the BMI program."""
    print("BMI Calculator")

    weight = get_weight()
    height_inches = get_height_inches()

    bmi = calculate_bmi(weight, height_inches)
    category = bmi_category(bmi)

    print("\nYour BMI is:", round(bmi, 1))
    print("Category:", category)

    print("\nBMI Legend:")
    print("Underweight: < 18.5")
    print("Healthy:     18.5 - 24.9")
    print("Overweight:  25.0 - 29.9")
    print("Obesity:     30.0+")


main()