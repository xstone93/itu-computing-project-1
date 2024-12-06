"""
IT:U Weather Station Analysis
------------------------------
This script is the starting point for analyzing the weather station dataset. 
Follow the tasks outlined in your instructions to complete the project.

Make sure to implement each function in its respective placeholder below.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Task 1: Load and explore the dataset
def load_dataset(file_path):
    """
    Loads the dataset from the given file path.

    Parameters:
        file_path (str): Path to the CSV file.

    Returns:
        DataFrame: Loaded weather dataset.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


# Task 2: Analyze temperature data
def analyze_temperature(data):
    """
    Placeholder function for Task 2.
    Calculate the minimum, maximum, and average temperature values.

    Parameters:
        data (DataFrame): The weather dataset.

    Returns:
        dict: A dictionary containing the min, max, and average temperatures.
    """
    pass  # TODO: Implement this function


# Task 3: Count weather conditions
def analyze_weather_conditions(data):
    """
    Placeholder function for Task 3.
    Count the occurrences of each weather condition.

    Parameters:
        data (DataFrame): The weather dataset.

    Returns:
        dict: A dictionary where keys are weather conditions and values are their counts.
    """
    pass  # TODO: Implement this function


# Task 4: Identify extreme weather days
def identify_extreme_weather_days(data, condition):
    """
    Placeholder function for Task 4.
    Identify all the days with a specific weather condition.

    Parameters:
        data (DataFrame): The weather dataset.
        condition (str): The specific weather condition to filter (e.g., "Rainy").

    Returns:
        list: A list of dates where the specified condition occurred.
    """
    pass  # TODO: Implement this function


# Task 5: Visualize weather conditions
def visualize_weather_conditions(data):
    """
    Placeholder function for Task 5.
    Create a visualization of the frequency of each weather condition.

    Parameters:
        data (DataFrame): The weather dataset.

    Returns:
        None: Displays a chart.
    """
    pass  # TODO: Implement this function


# Task 6: Calculate mean temperature for each month
def calculate_monthly_mean_temperature(data):
    """
    Placeholder function for Task 6.
    Calculate the mean temperature for each month.

    Parameters:
        data (DataFrame): The weather dataset.

    Returns:
        list: A list of 12 mean temperatures for each month (January to December).
    """
    pass  # TODO: Implement this function


# Task 7: Visualize monthly mean temperatures
def visualize_monthly_mean_temperature(mean_temperatures):
    """
    Placeholder function for Task 7.
    Create a bar chart to represent the mean temperature for each month.

    Parameters:
        mean_temperatures (list): A list of 12 mean temperature values.

    Returns:
        None: Displays a bar chart.
    """
    pass  # TODO: Implement this function


# Main program
def main():
    print("IT:U Weather Station Analysis")
    print("------------------------------")

    # Load the dataset
    file_path = "weather_data_2023_linz.csv"  # Replace with the actual file path
    data = load_dataset(file_path)

    if data is not None:
        # Explore the dataset (you can print the first few rows here)
        print("Dataset loaded successfully.")
        print(data.head())

        # Call your task functions here as you implement them
        # Example:
        # temp_analysis = analyze_temperature(data)
        # print(temp_analysis)

if __name__ == "__main__":
    main()
