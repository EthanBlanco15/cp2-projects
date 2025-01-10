#Ethan Blanco, Finalcial Calculator

def main():
    while True:
        main()

def goal_saving(mon): #This function is supposed to take how much the user wants to earn to then calculate how many reasonable days it would take.
    mon = input()
    mon/35
    goal_saving()

def budget_calc(): 
    
    budget_calc()

def sale_calc(price, sale): #This function is supposed to take the original price and multiply the percentage sale to calculate the real price.
    price = input()
    sale = input()
    price*sale
    sale_calc()

def tip_calc(cash): #This function is supposed to take how much the user has "paid", then divide that by 15
    cash = input()
    cash/15
    tip_calc()

calc = input("""Welcome to financial calculator, what would you like to do first?
            A. Calculate how long it will take to save for a goal.
            B. Budget allocator.
            C. Sale price.
            D. Tip calculation.\n""")
if calc == "a" and "A":
    mon = int(input("How much money would you like to earn?"))
    print(f"This is how many days it would take to achieve your financial goal {calc}")
if calc == "b" and "B":
    budget = input("What is your budget for the week?")
if calc == "c" and "C":
    price = int(input("Type in the original price"))
    sale = int(input("Type in the sale percentage, but convert it into a decimal (50% = 0.5)"))
    print(f"Here's the converted price with the sale {calc}")
if calc == "d" and "D":
    cash = int(input("How much did you pay?"))
    print(f"This is much you're paying for tips {cash}")
else:
    print("This doesn't work, re-enter to try again.")