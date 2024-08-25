# An application that tracks the amount of buyers for a total of 20 tickets available for purchase.
# The user can request to buy a certain number of tickets between 1 and 4 until all tickets are sold out.

def ticket_tracker():
    total_tickets = 20
    total_buyers = 0

    # Loop until all tickets are sold.
    while total_tickets > 0:

        while True:

            # Prompt the user for the number of tickets they want to buy.
            user_input = input("How many tickets would you like to purchase? (1-4): ")

            # check if the input is a number
            if user_input.isdigit():
                tickets_bought = int(user_input)
                break
            else:
                print("Error! Invalid input. Please enter a number.")

        # Confirm the requested number of tickets.
        if 1 <= tickets_bought <= 4:

            # Check if there are enough tickets to buy.
            if tickets_bought <= total_tickets:
                total_tickets -= tickets_bought
                total_buyers += 1

                print(f"Your transaction has been processed! Remaining tickets: {total_tickets}")

            else:
                print(f"Error! Not enough seats. Only {total_tickets} tickets remaining.")
        else:
            print(" Error! You are allowed to only purchase between 1 and 4 tickets")

    # Display the total number of buyers after all tickets are sold.
    print(f"All tickets are sold out! Total buyers: {total_buyers}")


ticket_tracker()
