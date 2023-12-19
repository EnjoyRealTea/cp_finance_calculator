# ============ Task 05 ==============
# ======== Capstone Project =========
# ********** E. Thompson ************

# -----------------------------------------------------------------------------------
# This program will allow a user to access two different financial calculators: 
# An investment calculator and a home loan repayment calculator.
# -----------------------------------------------------------------------------------

"""Start
    1. Ask the user which calculation they wish to do, with information given to help them choose.
    2. Show an error message if their input is invalid
    3. If 'investment' is selected:
        a) Ask the user to input the amount they are depositing.
        b) Ask the user to input the interest rate as a %.
        c) Ask the user to input the number of years they plan on investing.
        d) Ask the user to input if they want 'simple' or 'compound' interest.
        e) Calculate and output the amount of interest earned.
    4. If 'bond' is selected:
        a) Ask the user to input the present house value.
        b) Ask the user to input the interest rate.
        c) Ask the user for the number of months they wish to repay over.
        d) Calculate and output the monthly repayment amount.
   End"""

import math

# Asks user which calculation they would like to perform:

print("""
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan\n""")

calculation_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").upper()
# (The user's input is converted to uppercase so that it is not case-sensitive.)


# --------------------Investment option:----------------------

if calculation_type == "INVESTMENT":
    # Asks for the required variables from the user:
    # NB: Float is used for deposit because money is typically in 0.00 format, the user may want to invest e.g. £100.50
    #     Similarly, float is used for interest rate because it is often not a whole number, e.g. 5.25%.

    deposit_amount = float(input("\nPlease enter the amount of money you wish to deposit\t\t\t\t: "))
    interest_rate = float(input("Please enter the interest rate percentage (e.g. for '5%' enter '5')\t: "))
    invest_years = int(input("Please enter the number of years you plan to invest for\t\t\t\t: "))
    interest_type = input("\nPlease enter either 'simple' or 'compound' for your interest type:  ").upper()
    # Upper() removes case-sensitivity

    interest_rate_dec = interest_rate / 100  # Both calculations require the interest rate in decimal format.

    if interest_type == "SIMPLE":
        # Uses the simple interest formula A = P(1 + r*t) where P = deposit, r = rate as a decimal, t = time in years:

        interest_amount = deposit_amount * (1 + interest_rate_dec * invest_years)

        print(f"\n\tYou would earn {round(interest_amount, 2)} over {invest_years} years, with a simple interest "
              f"rate of {interest_rate} %.")

    elif interest_type == "COMPOUND":
        # Uses the compound interest formula A = P(1 + r)^t where P = deposit, r = rate as a decimal, t = time in years:

        interest_amount = deposit_amount * math.pow((1 + interest_rate_dec), invest_years)

        print(f"\n\tYou would earn {round(interest_amount, 2)} over {invest_years} years, with a compound interest "
              f"rate of {interest_rate} %.")

    else:
        # This message is shown if the input was not "simple" or "compound":
        print(f"'{interest_type}' is not a valid interest type, please try again and enter either 'simple' "
              f"or 'compound'.")


# ----------------------Bond option:---------------------------

elif calculation_type == "BOND":
    # Asks for the required variables from the user:
    # NB: Float is used for interest rate because it is often not a whole number, e.g. 5.25%.

    house_value = int(input("\nPlease enter the present value of the house (e.g. 100000)\t\t\t: "))
    interest_rate = float(input("Please enter the interest rate percentage (e.g. for '5%' enter '5')\t: "))
    repay_time_months = int(input("Please enter the number of months you plan to repay the loan over\t: "))

    # Calculates the monthly repayment amount using the formula A = i x P / 1 - (1 + i)^-n
    # where P is the house value, i the monthly interest rate as a decimal, n the number of months:

    monthly_interest_rate = (interest_rate / 100) / 12

    repayment_amount = (monthly_interest_rate * house_value) / (
            1 - (1 + monthly_interest_rate) ** (- repay_time_months))

    print(f"\n\tYou would need to repay {round(repayment_amount, 2)} each month.")


# --------------------Invalid option:----------------------------

else:
    # This message is shown if the input was not "Investment" or "Bond":
    print(f"'{calculation_type}' is not a valid entry, please try again and enter either 'investment' or 'bond'.")
