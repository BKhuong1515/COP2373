# Name: Brandon Nguyen
# Date Created: 10/14/24
# Assignment: Exercise 6A

# This program allows the user to input multiple sentences, 
# then numbers and displays each sentence entered by the user.

import re


def get_sentences(text):
    # Pattern to determine sentences
    pat = r'([A-Z0-9][^.!?]*[.!?]?)'
    sentences = re.findall(pat, text, flags=re.MULTILINE | re.DOTALL)
    return sentences


def main():
    print("Enter any number of sentences (type '1' when you're ready to see the sentence count):")
    input_text = ""

    # Loop to collect user input until '1' is entered
    while True:
        end_input = input()
        if end_input.strip().upper() == '1':
            break
        input_text += end_input + "\n"

    # Get and display the sentences
    sentences = get_sentences(input_text)

    print("\nSentences:")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")


main()
