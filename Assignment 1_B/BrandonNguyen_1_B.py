# Name: Brandon Nguyen
# Assignment: Exercise 1B
# Program that acts as a Magic 8 Ball and gives a random response to a yes/no questions asked by the user.

import random

RESPONSES_FILE = "8ball_responses.txt"


# Create a file with Magic 8 Ball responses
def create_file():

    # List of Magic 8 Ball responses
    response_list = [
        "Yes, of course!",
        "Without a doubt, yes.",
        "You can count on it.",
        "For sure!",
        "Ask me later!",
        "I'm not sure.",
        "I can't tell you right now.",
        "I'll tell you after my nap.",
        "No way!",
        "I don't think so.",
        "Without a doubt, no.",
        "The answer is clearly NO!"
    ]

    # Save the responses to a file
    with open(RESPONSES_FILE, "w") as file:
        for response in response_list:
            file.write(response + "\n")


# Load responses from the file
def get_responses():
    # Read the responses from the file and return them as a list
    with open(RESPONSES_FILE, "r") as file:
        responses_list = [response.strip() for response in file.readlines()]

    return responses_list


# Handle the Magic 8 Ball game
def magic8_ball():
    # Load the list of responses
    responses_list = get_responses()

    while True:
        # Ask the user for a yes/no question
        user_input = input("Ask a yes/no question (or type 'quit' to exit): ")

        # Exit the loop if user types quit
        if user_input.lower() == 'quit':
            print("You have successfully quit the program!")
            break

        # Choose a random response from the list
        magic8_response = random.choice(responses_list)

        # Display the Magic 8 Ball response
        print("The Magic 8 Ball says:", magic8_response)
        print()


# Run the program
def main():
    # Create the file with responses
    create_file()

    # Initiate the Magic 8 Ball
    magic8_ball()


main()
