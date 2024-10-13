# Name: Brandon Nguyen
# Date Created: 10/03/24
# Assignment: Exercise 6A
#
# Program Description:
# This program allows the user to input a phone number, social security number (SSN), and zip code.
# It then validates each input using regular expressions to determine if the values match the formats for each type.

import re

# Validation rules for phone, ssn, and zip code.
GET_DATA_FORMAT = {

    # Accept format (XXX) XXX-XXXX, XXX-XXX-XXXX, or XXXXXXXXXX.
    "phone_number": r'^(\(\d{3}\)\s|\d{3}-|\d{3})\d{3}-?\d{4}$',

    # Accept format XXX-XX-XXXX or XXXXXXXXX.
    "ssn": r'^(\d{3}-\d{2}-\d{4}|\d{9})$',

    # Accept format XXXXX or XXXXX-XXXX.
    "zip_code": r'^\d{5}(-\d{4})?$'
}


# Validate input based on format
def validate_format(input_value, pattern, input_type):
    if re.match(pattern, input_value):
        print(f"{input_value} is valid for {input_type}.")
    else:
        print(f"{input_value} is invalid for {input_type}.")


# Main function to get user input and validate the entries
def main():
    # Get user input, only display one acceptable format for simplicity.
    phone_number = input("Enter a phone number as XXX-XXX-XXXX: ")
    ssn = input("Enter a Social Security Number as 'XXX-XX-XXXX: ")
    zip_code = input("Enter a ZIP code as XXXXX: ")

    # Validate inputs
    validate_format(phone_number, GET_DATA_FORMAT["phone_number"], "phone number")
    validate_format(ssn, GET_DATA_FORMAT["ssn"], "Social Security Number")
    validate_format(zip_code, GET_DATA_FORMAT["zip_code"], "ZIP code")


main()
