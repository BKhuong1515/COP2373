# Name: Brandon Nguyen
# Assignment: Exercise 2A
# Program scans an email message for spam keywords, assigns a score, and rates the likelihood of the message being spam.

# List of spam words
SPAM_KEYWORDS = [
    'While supplies last', 'Quote', 'Clearance', 'Guaranteed', 'Free money',
    'Take action', 'Luxury', 'See for yourself', 'Deal', 'Exclusive',
    '100% free', '100% satisfied', 'Free gift', 'Lower rates', 'Best price', 'Cancel at any time',
    'Reserves the right', 'Bulk email', 'No catch', 'No strings attached',
    'Eliminate bad credit', 'Free investment', 'Full refund', 'Confidentiality',
    'Important information regarding', 'Unsecured credit', 'Expect to earn',
    '100% satisfied', 'Direct email', 'Save big money', 'Refinance',
    'Earn money', 'Big bucks', 'Act now', 'Apply now', 'Register', 'Savings'
]


def calculate_score(message):
    spam_score = 0
    flagged_words = []

    # check for lowercase words
    message_lower = message.lower()

    # Check for occurrences of spam words
    for keyword in SPAM_KEYWORDS:
        if keyword.lower() in message_lower:
            spam_score += 1
            flagged_words.append(keyword)

    return spam_score, flagged_words


def rating(score):
    if score == 0:
        return "Very unlikely"
    elif score < 5:
        return "Unlikely"
    elif score < 10:
        return "Likely"
    else:
        return "Very likely"


def main():
    # Get input email message from the user
    message = input("Enter a email message to check for spam: ")

    # get flagged words/phrases and calculate score
    spam_score, flagged_words = calculate_score(message)

    # Rate the likelihood of spam
    spam_rating = rating(spam_score)

    # Display the results
    print(f"\nSpam Score: {spam_score}")
    print(f"Likelihood of being spam: {spam_rating}")

    if flagged_words:
        print("\nFlagged words/phrases:")
        for word in flagged_words:
            print(f" - {word}")
    else:
        print("No spam words found!")


main()
