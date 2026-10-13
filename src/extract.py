import pandas as pd


def extract_data(file_path):
    """
    Extracts data from a CSV file and returns it as a pandas DataFrame.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the extracted data.
    """
    return pd.read_csv(file_path)
