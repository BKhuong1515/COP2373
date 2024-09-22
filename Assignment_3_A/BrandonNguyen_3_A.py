# Name: Brandon Nguyen
# Assignment: Exercise 3A
# This program allows the user to input different expenses and then calculates 
# the total expense, as well as finding the highest and lowest expense amounts.

from functools import reduce


# Function to find the highest expense
def expense_highest(expenses):
    return reduce(
        lambda current_expense, next_expense:
        current_expense if current_expense[1] > next_expense[1] else next_expense,
        expenses
    )


# Function to find the lowest expense
def expense_lowest(expenses):
    return reduce(
        lambda current_expense, next_expense:
        current_expense if current_expense[1] < next_expense[1] else next_expense,
        expenses
    )


# Function to calculate total expenses
def expense_total(expenses):
    return reduce(lambda total, expense: total + expense[1], expenses, 0)


def main():
    expenses = []  # List to store the user's expenses

    # Loop to ask the user for their expenses
    # The loop continues until the user types '1'
    while True:
        expense_type = input("Please enter the expense type (or type '1' to complete): ")
        if expense_type == '1':
            break
        try:
            # Convert the expense amount to a float and store it with the type
            amount = float(input(f"Enter the amount for {expense_type}: $"))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Error! Invalid input for amount.")

    # Check if the expenses list is empty
    if not expenses:
        print("No expenses entered. Exiting the program.")
        return

    # Find the highest, lowest expenses and calculate the total
    total_expense = expense_total(expenses)
    highest_expense = expense_highest(expenses)
    lowest_expense = expense_lowest(expenses)

    # Format and display the results to the user
    print(f"\nTotal expenses: ${total_expense:.2f}")
    print(f"Highest expense: {highest_expense[0]} (${highest_expense[1]:.2f})")
    print(f"Lowest expense: {lowest_expense[0]} (${lowest_expense[1]:.2f})")


main()
