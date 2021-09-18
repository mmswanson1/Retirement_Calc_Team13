from retirementCalc import *


def main():

    print("\nSocial Security Full Retirement Age Calculator\n")

    while True:
        birth_year = input("Enter the year of birth or enter to exit: ")
        if not birth_year:
            break

        birth_month = int(input("Enter the numerical month of birth: "))

        years, months = calculate_age(birth_year)
        month_str = display_month(months, birth_month)
        retire_year = calculate_year(birth_year, years, birth_month, months)

        print("\tYour full retirement age is ", years, " and ", months, " months")
        print("\tThis will be in ", month_str, " of ", retire_year)
        print()


main()
