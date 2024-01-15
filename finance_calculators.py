"""
a program that allows the user to access two financial calculators:
an investment calculator and a home loan repayment calculator
"""

import math


class FinancialCalculators:
    @staticmethod
    # Define a function to get valid numeric input
    def get_validated_numeric_input(prompt):
        # Continuously prompt for input until a valid numeric value is entered
        while True:
            try:
                value = float(input(prompt))
                # Return the valid numeric value
                return value
            except ValueError:
                # Display error message for invalid input
                print("Invalid input. Please enter a numeric value.")

    @staticmethod
    # Function to calculate and display investment interest
    def investment_interest():
        try:
            principal = FinancialCalculators.get_validated_numeric_input("Please enter the principal "
                                                                         "amount you would like to deposit: ")
            interest_rate = FinancialCalculators.get_validated_numeric_input("Please enter the annual "
                                                                             "interest rate: ")
            interest = interest_rate / 100
            time = FinancialCalculators.get_validated_numeric_input("How many years you would like to invest for: ")
            interest_type = input("Please select the interest type. Enter 's' for simple interest "
                                  "or 'c' for compound': ").lower()
            if interest_type not in ["s", "c"]:
                print("Invalid selection. Please type 's' for simple interest or 'c' for compound.")
                return  # Exit the function if the input is invalid

                # Calculate the total amount based on the selected interest type
            if interest_type == "s":  # If simple calculate using simple interest formula
                interest_earned = principal * (1 + interest * time) 
                print(f"You will be earning £{round(interest_earned)} in interest if you invest £{principal} "
                      f"for {time} years.")
                return interest_earned

            elif interest_type == "c":  # If compound calculate using compound interest formula
                interest_earned_c = principal * math.pow((1 + interest), time)
                print(f"You will be earning £{round(interest_earned_c)} in interest if you invest £{principal} "
                      f"for {time} years.")
                return interest_earned_c  # Exit the function after successful calculation
        except ValueError:
            print("Invalid input. Please enter a numeric value. ")

    @staticmethod
    # Function to calculate and display bond repayment amount
    def bond_interest():
        try:
            house_value = FinancialCalculators.get_validated_numeric_input("Please enter the present value of the "
                                                                           "house: ")
            interest = FinancialCalculators.get_validated_numeric_input("Please enter the annual interest rate "
                                                                        "(as a percentage): ")
            monthly_interest = interest / 12 / 100
            time = FinancialCalculators.get_validated_numeric_input("Enter a number of months over which "
                                                                    "the bond will be repaid: ")

            # Check if time is 0 to prevent division by zero
            if time == 0:
                print("Invalid input. The repayment period must be greater than 0.")

            # Calculate the monthly repayment amount
            monthly_repayment = (monthly_interest * house_value) / (1 - (1 + monthly_interest) ** (-time))

            # Display monthly repayment amount
            print(f"If you take a bond for £{house_value} in house value, for {time} months, with the annual interest "
                  f"rate of {interest}% - your monthly payment will be equal to:  £{round(monthly_repayment)}")
            return monthly_repayment  # Exit the function after successful calculation

        except ZeroDivisionError:
            print("You cannot divide by 0. ")


def main():
    # Display menu options and prompt for user selection
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond - to calculate the amount you'll have to pay on a home loan")
    choice = input("\n\nEnter 'i' to carry out an investment or 'b' to carry out bond:").lower()

    # Validate user selection
    while choice not in ["i", "b"]:
        print("Invalid selection. Please enter either 'i' for investment or 'b' for bond.")
        choice = input("Please enter either 'investment' or 'bond' to proceed:").lower()

    #  Create a variable for the financial calculator class
    calculator = FinancialCalculators()

    # Execute the selected function based on user choice
    if choice == "b":
        calculator.bond_interest()
    elif choice == "i":
        calculator.investment_interest()


if __name__ == "__main__":
    main()
