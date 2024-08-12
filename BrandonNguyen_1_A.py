# Ticket Sales Program
# Name: Brandon Nguyen
# Assignment: 1A
# A application where 20 tickets are available for purchase.
# The user can request to buy a certain number of tickets between 1 and 4 until all tickets are sold out.
# Also, keeps track of the remaining tickets and the total number of buyers.

def sell_tickets():
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
                print("Invalid input. Please enter a number.")

        # Confirm the requested number of tickets.
        if 1 <= tickets_bought <= 4:

            # Check if there are enough tickets to buy.
            if tickets_bought <= total_tickets:
                total_tickets -= tickets_bought
                total_buyers += 1
                print(f"Tickets successfully purchased! Remaining tickets: {total_tickets}")
            else:
                print(f"Sorry, only {total_tickets} tickets remaining.")
        else:
            print("You can only buy between 1 and 4 tickets.")

    # Display the total number of buyers after all tickets are sold
    print(f"All tickets are sold out! Total buyers: {total_buyers}")


sell_tickets()
