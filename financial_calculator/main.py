# Ethan Blanco, Financial Calculator

# Import necessary modules
import math

def goal_saving(goal_amount, deposit_amount, frequency):
# This function to calculate the time required to save for a goal
    if deposit_amount <= 0:
        return "Deposit amount must be greater than zero."
    term = math.ceil(goal_amount / deposit_amount)
    return term if frequency.lower() == 'weekly' else term // 4

def comp_interest(principal, rate, times_comp, years):
# Compound interest calculator
    if principal < 0 or rate < 0 or times_comp <= 0 or years < 0:
        return "Invalid inputs. Ensure values are positive."
    return principal * (1 + rate / (100 * times_comp))**(times_comp * years)

def budget_allocator(income, percentages):
# Budget allocator
    allocation = {}
    for category, percentage in percentages.items():
        allocation[category] = income * (percentage / 100)
    return allocation

def sale_price(original_sale, discount_price):
# This function is supposed to take the original sale price then multiply it by the discount.
    if original_sale < 0 or discount_price < 0 or discount_price > 100:
        return "Invalid inputs for sale price."
    return original_sale * (1 - discount_price / 100)

def tip_calc(cash, tip_percent):
# This function is supposed to take how much the user has paid, then divide.
    if cash < 0 or tip_percent < 0:
        return "Invalid inputs for tip."
    return cash * (tip_percent / 100)

# Main function to run the user interface
def main():
    while True:
        print("\nChoose a financial calculator problem:")
        print("1. Goal saving Calculator")
        print("2. Compound Interest Calculator")
        print("3. Budget Allocator Calculator")
        print("4. Sale Price Convert Calculator")
        print("5. Tip Convert Calculator")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            goal_amount = float(input("Enter the savings goal amount: "))
            deposit_amount = float(input("Enter the weekly/monthly deposit amount: "))
            frequency = input("Is this deposit weekly or monthly? ").strip().lower()
            result = goal_saving(goal_amount, deposit_amount, frequency)
            print(f"Time to save: {result} {frequency}s")
        elif choice == "2":
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the annual interest rate (in %): "))
            times = int(input("Enter the number of times interest is compounded annually: "))
            years = float(input("Enter the number of years: "))
            result = comp_interest(principal, rate, times, years)
            print(f"Compound interest result: {result}")
        elif choice == "3":
            income = float(input("Enter your total income: "))
            print("Enter budget allocation percentages for categories (e.g., savings, food):")
            categories = {}
            while True:
                category = input("Category name (or type 'done' to finish): ").strip()
                if category.lower() == 'done':
                    break
                percentage = float(input(f"Enter percentage for {category}: "))
                categories[category] = percentage
            result = budget_allocator(income, categories)
            print("Budget Allocation:")
            for cat, amount in result.items():
                print(f"{cat}: {amount:.2f}")
        elif choice == "4":
            original_sale = float(input("Enter the original price: "))
            discount_price = float(input("Enter the discount percentage: "))
            result = sale_price(original_sale, discount_price)
            print(f"Sale price: {result:.2f}")
        elif choice == "5":
            cash = float(input("Enter the bill amount: "))
            tip_percent = float(input("Enter the tip percentage: "))
            result = tip_calc(cash, tip_percent)
            print(f"Tip amount: {result:.2f}")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run program
if __name__ == "__main__":
    main()