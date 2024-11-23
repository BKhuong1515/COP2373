# Name: Brandon Nguyen
# Date Created: 11/17/24
# Assignment: Exercise 12A

# Program Description:
# Loads student grades from a CSV file, then calculates and
# displays the mean, median, standard deviation, minimum, and maximum for each exam and overall grades.
# Also determines pass/fail statistics and calculates the overall pass percentage.

import numpy

# CONSTANT for passing grade
PASSING_GRADE = 60


def load_data(file_name):
    try:
        # Load data from the file and select the grade columns
        data = numpy.genfromtxt(file_name, delimiter=',', skip_header=1, dtype=float, usecols=(2, 3, 4))

        # Display the loaded data from csv
        print("\n-----Loaded Data-----")
        print(data)
        return data

    except FileNotFoundError:

        # If file is not found display error
        print(f"Error: File '{file_name}' not found. Please ensure it exists in the directory.")
        return None


def calculate_statistics(data):

    # Calculate and display statistics for each exam and overall grades.
    if data is None:
        print("No data loaded.")
        return

    print("\n-----Statistics for Each Exam-----")

    # Transpose the data to iterate through each exam
    for exam_index, exam in enumerate(data.T, start=1):
        # Display statistics for the current exam
        print(f"Exam {exam_index}:")
        print(f"  Mean: {numpy.mean(exam):.2f}")
        print(f"  Median: {numpy.median(exam):.2f}")
        print(f"  Std Dev: {numpy.std(exam):.2f}")
        print(f"  Min: {numpy.min(exam):.2f}")
        print(f"  Max: {numpy.max(exam):.2f}")

    # Flatten the data to calculate overall statistics
    overall_grades = data.flatten()

    print("\n-----Overall Statistics-----")
    print(f"Mean: {numpy.mean(overall_grades):.2f}")
    print(f"Median: {numpy.median(overall_grades):.2f}")
    print(f"Std Dev: {numpy.std(overall_grades):.2f}")
    print(f"Min: {numpy.min(overall_grades):.2f}")
    print(f"Max: {numpy.max(overall_grades):.2f}")


def calculate_pass_fail(data):
    if data is None:
        print("No data loaded.")
        return

    print("\n-----Pass/Fail Statistics-----")

    # Iterate through each exam
    total_passes = 0
    total_grades = data.size

    for exam_index, exam in enumerate(data.T, start=1):
        # Calculate number of passes and fails for the current exam
        passes = numpy.sum(exam >= PASSING_GRADE)
        fails = len(exam) - passes
        total_passes += passes

        # Display pass/fail stats for the current exam
        print(f"Exam {exam_index}: Passed = {passes}, Failed = {fails}")

    # Calculate the overall pass percentage
    overall_pass_percentage = (total_passes / total_grades) * 100

    # Display the overall pass percentage
    print(f"\nOverall Pass Percentage: {overall_pass_percentage:.2f}%")


def main():

    # Find grades.csv as the file name
    file_name = 'grades.csv'

    # Load data from the CSV file
    data = load_data(file_name)

    # If data is loaded, calculate and display statistics
    if data is not None:
        calculate_statistics(data)
        calculate_pass_fail(data)


# Run the main function
main()
