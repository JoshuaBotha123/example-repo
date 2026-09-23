import math

# Finance calculator: lets the user calculate the return on an investment
# or the monthly repayment on a home loan (bond).

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

choice = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").strip().lower()

if choice == "investment":
    deposit = float(input("Enter the amount of money you are depositing: "))
    rate = float(input("Enter the interest rate (as a number, e.g. 8 for 8%): ")) / 100
    years = int(input("Enter the number of years you plan on investing: "))
    interest = input("Do you want 'simple' or 'compound' interest? ").strip().lower()

    if interest == "simple":
        total = deposit * (1 + rate * years)
        print(f"Total amount after {years} years with simple interest: R{total:,.2f}")
    elif interest == "compound":
        total = deposit * math.pow(1 + rate, years)
        print(f"Total amount after {years} years with compound interest: R{total:,.2f}")
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")

elif choice == "bond":
    house_value = float(input("Enter the present value of the house: "))
    rate = float(input("Enter the annual interest rate (as a number, e.g. 7 for 7%): "))
    months = int(input("Enter the number of months to repay the bond: "))

    monthly_rate = (rate / 100) / 12
    repayment = (monthly_rate * house_value) / (1 - (1 + monthly_rate) ** (-months))
    print(f"Your monthly bond repayment will be: R{repayment:,.2f}")

else:
    print("Invalid option. Please enter either 'investment' or 'bond'.")
