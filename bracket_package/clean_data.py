def clean_data():
    """Clean the raw data by selecting specific columns and exporting the cleaned dataset.

    This function performs the following steps:
    1. Imports necessary packages (pandas and numpy).
    2. Prompts the user to input the path to the raw data file (CSV format).
    3. Reads the raw data into a pandas DataFrame.
    4. Selects specific columns ('TEAM', 'RANK', 'WIN', 'BARCLAW', 'SEED') from the raw data.
    5. Exports the cleaned data to a new CSV file named 'clean_data.csv' in the 'data' directory.

    Note:
    The user is prompted to input the path to the raw data file during execution.

    Args:
        None

    Returns:
        None
    """
    # Import packages
    import pandas as pd
    import numpy as np
    import os

    # Import raw data
    raw_data = pd.read_csv(input())

    # Clean data
    # Remove columns that are not needed
    # Grab any important columns: TEAM, RANK, WIN, BARCLAW, SEED:
    data = raw_data[['TEAM', 'RANK', 'WIN', 'BARCLAW', 'SEED']]
    data.to_csv('data/clean_data.csv', index=False)


if __name__ == '__main__':
    clean_data()
