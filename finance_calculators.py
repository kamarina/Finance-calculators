"""
a program that allows the user to access two financial calculators:
an investment calculator and a home loan repayment calculator
"""

import math
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


# Function to calculate and display investment interest
def investment_interest():
    keep_going = True
    while keep_going:
        try:
            principal = get_validated_numeric_input("Please enter the principal amount you would like to deposit: ")
            interest_rate = get_validated_numeric_input("Please enter the annual interest rate: ")
            interest = interest_rate / 100
            time = get_validated_numeric_input("How many years you would like to invest for: ")
            interest_type = input("Please enter the interest type 'simple' or 'compound': ").lower()
            if interest_type not in ["simple", "compound"]:
                print("Invalid selection. Please type 'simple' or 'compound'.")
                continue


            # Calculate the total amount based on the selected interest type
            if interest_type == "simple":
                total_amount = principal * (1 + interest * time)
                interest_earned = total_amount - principal
                print(f"You will be earning {round(interest_earned)} in interest if you invest {principal} for {time} years.")
                return interest_earned
            elif interest_type == "compound":
                total_amount = principal * math.pow((1 + interest), time)
                interest_earned = total_amount - principal
                print(f"You will be earning {interest_earned} in interest if you invest {principal} for {time} years.")
                return interest_earned
        except ValueError:
            print("Invalid input. Please enter a numeric value. ")


# Function to calculate and display bond repayment amount
def bond_interest():
    keep_going=True
    while keep_going:
        try:
            house_value = get_validated_numeric_input("Please enter the present value of the house: ")
            interest = get_validated_numeric_input("Please enter the annual interest rate (as a percentage): ")
            monthly_interest = interest / 12 / 100
            time = get_validated_numeric_input("Enter a number of months over which the bond will be repaid: ")

            # Check if time is 0 to prevent division by zero
            if time == 0:
                print("Invalid input. The repayment period must be greater than 0.")
                continue

            # Calculate the monthly repayment amount
            monthly_repayment = (monthly_interest * house_value) / (1 - (1 + monthly_interest) ** (-time))

            # Display monthly repayment amount
            print(f"If you take a bond for {house_value} in house value, for {time} months, with the annual interest rate of "
                f"{interest} - your monthly payment will be equal to:  {round(monthly_repayment)}")
            return monthly_repayment

        except ZeroDivisionError:
            print("You cannot divide by 0. ")

# Display menu options and prompt for user selection
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
choice = input("\n\nWould you like to carry out an 'investment' or 'bond':").lower()

# Validate user selection
while choice not in ["investment", "bond"]:
    print("Invalid selection. Please enter either 'investment' or 'bond'.")
    choice = input("Please enter either 'investment' or 'bond' to proceed:").lower()


# Execute the selected function based on user choice
if choice == "bond":
    bond_interest()
elif choice == "investment":
    investment_interest()

    
