# Name: Brandon Nguyen
# Date Created: 10/24/24
# Assignment: Exercise 8A

import csv


def read_student_data():

    try:
        # 'with' to ensure the file is closed properly
        with open('grades.csv', 'r') as file:
            reader = csv.reader(file)
            print("\n--- Student Grades ---\n")

            # Display the table header and rows
            for row in reader:
                print("{:<15} {:<15} {:<7} {:<7} {:<7}".format(*row))

    except FileNotFoundError:
        print(f"ERROR! grades.csv not found. Please ensure grades.csv file exists within the directory.")


read_student_data()
