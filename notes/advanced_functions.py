#Ethan Blanco, Advanced Functions Notes

#1. A helper function is a function called inside of a function to complete part of the task. function function function.
def check_input(user_text):

    return not any(char.isdigit() for char in user_text)


def hello(name):

    if check_input(name):
        print(f"hello {name}!")
    else:
        print("Please input only letters.")
        user = input("What is your name:\n").strip().capitalize()
        #8. Recursion is when you call a function inside of itself.
        hello(user)
        #9. Recursion runs the function itself again.


user = input("What is your name:\n").strip().capitalize()
hello(user)
#2. The helper functions make your functions simple.
#3. A function inside of another function is called an inner function.
def fun1(): #Wrapper functions, which mostly exists to keep the inner function safe from the rest of your code.
    
    msg = "This is the outer function"

    def fun2():
        print(msg)

    fun2()

fun1()
#4. The scope of a variable in a function with an inner function is Local, which includes the inner function.
#5. We use inner functions to have access to local variables without having to make it global and organization.
#6. A closure function is a variable to a function.
def fun(a):
    #Outer function remembers the value of a

    def adder(b):
        return a+b
    return adder #Returning the closure.

val = fun(10) #Easier if it's the same.

print(val[5]) #Easier if it changes.


#7. We write closer/inner functions and all of this to keep things safe and decrease the number of parameters.

def end(income):
    
    def calc(cost, type):
        percent = cost/income *100
        print(f"Your {type} is ${cost} and that is {percent:.0f}")
    return calc

def user_input(type):
    return int(input(f"What is your monthly {type}: $"))

income = user_input("Income")
rent = user_input("Rent")
utilities = user_input("Utilities")
transportation = user_input("Transportation")

ready = end(income)

ready(rent, "Rent")
ready(utilities, "Utilities")
ready(transportation, "Transportation")