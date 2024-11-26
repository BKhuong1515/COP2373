# Name: Brandon Nguyen
# Date Created: 11/20/24
# Assignment: Exercise 13_DB

# program simulates population growth for various cities in Florida over 2% growth for a 20-year period.
# Also utilizes a SQLite database to store population data and
# matplotlib to generate population growth plots for user-selected cities.


import matplotlib.pyplot as plt
import sqlite3

# Constants for database name and population growth rate
DB_NAME = "population_BN.db"
GROWTH_RATE = 0.02


def create_population_db():
    # Creates a SQLite database and initializes the population table.
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT NOT NULL,
            year INTEGER NOT NULL,
            population INTEGER NOT NULL,
            PRIMARY KEY (city, year)
        )
    """)

    # Initial data for 2023
    # Population data retrieved from https://www.florida-demographics.com/cities_by_population
    initial_population = [
        ("Miami", 2023, 455924),
        ("Orlando", 2023, 320742),
        ("Tampa", 2023, 403364),
        ("Bradenton", 2023, 57076),
        ("Tallahassee", 2023, 202221),
        ("Fort Myers", 2023, 97372),
        ("St. Petersburg", 2023, 263553),
        ("Sarasota", 2023, 57602),
        ("Gainesville", 2023, 145812),
        ("North Port", 2023, 88934),
    ]

    # Insert data if not already present
    cursor.executemany("""
        INSERT OR IGNORE INTO population (city, year, population)
        VALUES (?, ?, ?)
    """, initial_population)

    conn.commit()
    conn.close()


def population_growth():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Get all cities and their 2023 populations
    cursor.execute("SELECT city, population FROM population WHERE year = 2023")
    data = cursor.fetchall()

    # Loop through each city and calculate population growth for 20 years
    for city, population in data:
        current_population = population
        for year in range(2024, 2044):
            # Calculate the population for the next year
            current_population = int(current_population * (1 + GROWTH_RATE))

            # Insert the calculated population into the database
            cursor.execute("""
                INSERT OR IGNORE INTO population (city, year, population)
                VALUES (?, ?, ?)
            """, (city, year, current_population))

    conn.commit()
    conn.close()


def plot_population_growth():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Get list of cities from the database
    cursor.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cursor.fetchall()]

    while True:
        # Display available cities for user selection
        print("\nAvailable cities:")
        for i, city in enumerate(cities, 1):
            print(f"{i}. {city}")

        # Prompt user to select a city or exit
        choice = input("Select a city by number (or type '0' to exit): ").strip().lower()

        if choice == '0':
            break

        # Validate user input
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(cities):
            print("Invalid choice. Please try again.")
            continue

        # Retrieve the city based on the user's choice
        city = cities[int(choice) - 1]

        # Fetch population data for the selected city
        cursor.execute("SELECT year, population FROM population WHERE city = ? ORDER BY year", (city,))
        data = cursor.fetchall()

        # Extract years and population values for plot
        years = [row[0] for row in data]
        populations = [row[1] for row in data]

        # Plot the population growth for the selected city
        plt.figure(figsize=(10, 6))  # Set figure size for better readability
        plt.plot(years, populations, marker='o')  # Use marker plot to emphasize individual data points
        plt.title(f"Population Growth for {city}")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.grid(True)
        plt.show()

    conn.close()


def main():
    # Initialize the database and populate initial data
    create_population_db()

    # Simulate 20 years of population growth
    population_growth()
    plot_population_growth()


main()
