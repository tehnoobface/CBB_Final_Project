"""
This script imports the raw data, cleans it, and explorts the final dataset.
"""
def clean_data():
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