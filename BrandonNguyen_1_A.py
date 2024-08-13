# An application where a limited number of tickets are available for purchase.
# The user can request to buy a certain number of tickets between 1 and 4 until all tickets are sold out.
# Also, keeps track of the remaining tickets and the total number of buyers.

def ticket_tracker():
    total_tickets = 20
    total_buyers = 0

    # Loop until all tickets are sold
    while total_tickets > 0:

        # Prompt the user for the number of tickets they want to buy
        tickets_bought = int(input("How many tickets would you like to buy? (1-4): "))

        # Check the requested number of tickets
        if 1 <= tickets_bought <= 4:

            # Check if there are enough tickets to buy.
            if tickets_bought <= total_tickets:
                total_tickets -= tickets_bought
                total_buyers += 1

                print(f"Your transaction has been processed! Remaining tickets: {total_tickets}")

            else:
                print(f"Error! Only {total_tickets} tickets remaining.")
        else:
            print(" Error! You are allowed to purchase between 1 and 4 tickets")

        if total_tickets == 0:
            break

    # Display the total number of buyers after all tickets are sold
    print(f"All tickets are sold out! Total buyers: {total_buyers}")


ticket_tracker()
