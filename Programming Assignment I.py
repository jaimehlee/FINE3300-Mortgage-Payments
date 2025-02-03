# FINE3300-Mortgage-Payments: 
# Programming Assignment #1: Winter 2025 Edition  - Jaime Lee (FINE3300: Winter 2025)

import math

def mortgage_payments(principal, rate, amortization):
    rate = rate / 100
    rate_semi = (1 + rate / 2)
# The above attempts to define the function for semi-annual compounding (in decimal).

    rate_monthly = rate_semi ** (2 / 12) - 1
    rate_semi_monthly = rate_semi ** (2 / 24) - 1
    rate_bi_weekly = rate_semi ** (2 / 26) - 1
    rate_weekly = rate_semi ** (2 / 52) - 1
# Appropriate periodic rate formulas are stated above in reference to the assignment sheet notation.

    number_monthly = amortization * 12
    number_semi_monthly = amortization * 24
    number_bi_weekly = amortization * 26
    number_weekly = amortization * 52
# Determining the number of payments to be made over the defined/provided amortization period.

    def pva(r, n):
        return (1 - (1 + r) ** -n) / r
# Present Value of Annuity factor (pva) defined.

    monthly_payment = principal / pva(rate_monthly, number_monthly)
    semi_monthly_payment = principal / pva(rate_semi_monthly, number_semi_monthly)
    bi_weekly_payment = principal / pva(rate_bi_weekly, number_bi_weekly)
    weekly_payment = principal / pva(rate_weekly, number_weekly)
# Calculating the payment amount for each payment frequency.
# The principal is divided by the PVA factor for each stated case.

    rapid_bi_weekly_payment = monthly_payment / 2
    rapid_weekly_payment = monthly_payment / 4
# Defining the accelerated payments.

    return (
        round(monthly_payment, 2),
        round(semi_monthly_payment, 2),
        round(bi_weekly_payment, 2),
        round(weekly_payment, 2),
        round(rapid_bi_weekly_payment, 2),
        round(rapid_weekly_payment, 2)
    )
# Ensuring the function returns a tuple containing the rounded payment values in the appropriate standardized currency notation.

if __name__ == "__main__":
    principal = float(input("Enter Principal Amount: "))
    rate = float(input("Enter Quoted Interest Rate (i.e., 4.85 for 4.85%): "))
    amortization = int(input("Enter Amortization Period in Years: "))
# Prompting the user to input the loan principal, interest rate, and amortization years; defined as a float, float, and integer, respectively.

    results = mortgage_payments(principal, rate, amortization)
# Calling the function and saving the results in 'results'.

    print("\nMortgage Payment Breakdown:")
    print(f"Monthly Payment: ${results[0]:,.2f}")
    print(f"Semi-monthly Payment: ${results[1]:,.2f}")
    print(f"Bi-weekly Payment: ${results[2]:,.2f}")
    print(f"Weekly Payment: ${results[3]:,.2f}")
    print(f"Accelerated Bi-weekly Payment: ${results[4]:,.2f}")
    print(f"Accelerated Weekly Payment: ${results[5]:,.2f}")
# Adding commas and rounding the results within two decimal places.